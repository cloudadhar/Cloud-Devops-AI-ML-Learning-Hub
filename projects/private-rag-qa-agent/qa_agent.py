from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from typing import Any

from langchain.agents import create_agent
from langchain.agents.middleware import AgentMiddleware, AgentState
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader


DEFAULT_DOCS_DIR = "documents"
DEFAULT_DB_DIR = "chroma_db"
DEFAULT_CHAT_MODEL = "qwen3:4b"
DEFAULT_EMBED_MODEL = "nomic-embed-text"

SYSTEM_PROMPT = """You answer questions only from the retrieved context.
If the context does not contain the answer, say that you do not know.
Keep answers clear for learners and mention the source files used."""


class RagState(AgentState):
    context: list[Document]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Private local RAG Q&A agent")
    parser.add_argument("--docs", default=DEFAULT_DOCS_DIR, help="Folder containing PDF, Markdown, and text files")
    parser.add_argument("--db", default=DEFAULT_DB_DIR, help="Folder for the local Chroma database")
    parser.add_argument("--chat-model", default=DEFAULT_CHAT_MODEL, help="Ollama chat model")
    parser.add_argument("--embed-model", default=DEFAULT_EMBED_MODEL, help="Ollama embedding model")
    parser.add_argument("--k", type=int, default=5, help="Number of chunks to retrieve per question")
    parser.add_argument("--chunk-size", type=int, default=1000, help="Maximum characters per chunk")
    parser.add_argument("--chunk-overlap", type=int, default=200, help="Overlapping characters between chunks")
    parser.add_argument("--reindex", action="store_true", help="Delete and rebuild the vector database")
    return parser.parse_args()


def read_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def load_documents(docs_dir: Path) -> list[Document]:
    supported = {".md", ".txt", ".pdf"}
    documents: list[Document] = []

    for path in sorted(docs_dir.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in supported:
            continue

        if path.suffix.lower() == ".pdf":
            content = read_pdf(path)
        else:
            content = path.read_text(encoding="utf-8", errors="ignore")

        content = content.strip()
        if content:
            documents.append(Document(page_content=content, metadata={"source": str(path)}))

    return documents


def build_vector_store(args: argparse.Namespace) -> Chroma:
    docs_dir = Path(args.docs)
    db_dir = Path(args.db)
    embeddings = OllamaEmbeddings(model=args.embed_model)

    if args.reindex and db_dir.exists():
        shutil.rmtree(db_dir)

    if db_dir.exists():
        return Chroma(
            collection_name="private_rag_documents",
            persist_directory=str(db_dir),
            embedding_function=embeddings,
        )

    documents = load_documents(docs_dir)
    if not documents:
        raise SystemExit(f"No supported files found in {docs_dir}. Add .pdf, .md, or .txt files first.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap,
    )
    chunks = splitter.split_documents(documents)

    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="private_rag_documents",
        persist_directory=str(db_dir),
    )


def format_context(documents: list[Document]) -> str:
    blocks = []
    for index, doc in enumerate(documents, start=1):
        source = doc.metadata.get("source", "unknown")
        blocks.append(f"[{index}] Source: {source}\n{doc.page_content}")
    return "\n\n".join(blocks)


class RetrievalMiddleware(AgentMiddleware[RagState]):
    state_schema = RagState

    def __init__(self, vector_store: Chroma, k: int):
        self.vector_store = vector_store
        self.k = k

    def before_model(self, state: RagState) -> dict[str, Any] | None:
        question = str(state["messages"][-1].content)
        matches = self.vector_store.similarity_search(question, k=self.k)
        context = format_context(matches)

        return {
            "messages": [
                SystemMessage(content=f"{SYSTEM_PROMPT}\n\nRetrieved context:\n{context}")
            ],
            "context": matches,
        }


def build_agent(vector_store: Chroma, args: argparse.Namespace):
    model = ChatOllama(model=args.chat_model, temperature=0)
    return create_agent(
        model=model,
        tools=[],
        middleware=[RetrievalMiddleware(vector_store, args.k)],
        state_schema=RagState,
    )


def print_sources(documents: list[Document]) -> None:
    seen: set[str] = set()
    print("\nSources:")
    for doc in documents:
        source = doc.metadata.get("source", "unknown")
        if source not in seen:
            print(f"- {source}")
            seen.add(source)


def main() -> None:
    args = parse_args()
    vector_store = build_vector_store(args)
    agent = build_agent(vector_store, args)

    print("Private RAG agent is ready. Ask a question, or type exit.")
    while True:
        question = input("\nYou: ").strip()
        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue

        result = agent.invoke({"messages": [{"role": "user", "content": question}], "context": []})
        print(f"\nAnswer:\n{result['messages'][-1].content}")
        print_sources(result.get("context", []))


if __name__ == "__main__":
    main()
