# Machine Learning

![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)

## Who This Track Is For

Learners targeting ML fundamentals, data science basics, model training, model evaluation, and technical interviews.

## Outcomes

- Understand supervised, unsupervised, classification, regression, features, labels, train/test split, cross-validation, and metrics.
- Train models using scikit-learn and understand when deep learning frameworks like PyTorch/TensorFlow are useful.
- Explain model behavior, overfitting, underfitting, data leakage, bias, variance, and feature importance.


## Architecture Mental Model

```text
Raw data -> cleaning -> feature engineering -> train/test split -> model training -> evaluation -> model artifact -> explanation -> handoff to MLOps
```

## 30-60-90 Day Learning Flow

### First 30 Days

- Learn Python, NumPy, Pandas, data cleaning, visualization basics, and scikit-learn estimator pattern.
- Train classification and regression models and compare metrics.
- Practice train/test split and cross-validation to avoid misleading results.

### Days 31-60

- Learn pipelines, preprocessing, hyperparameter search, model selection, and feature importance.
- Practice imbalanced data, missing values, outliers, and leakage prevention.
- Write model cards explaining data, limitations, metrics, and risks.

### Days 61-90

- Learn deep learning basics with PyTorch or TensorFlow: tensors, layers, loss, optimizer, training loop.
- Create one end-to-end ML project with reproducible notebook and saved model.
- Prepare handoff notes for MLOps deployment.

## Hands-on Labs

- Train a churn prediction model with proper train/test split.
- Build a house price regression model and explain MAE/RMSE.
- Create a fraud or anomaly detection experiment and discuss false positives.
- Write a model card for every project.

## Scenario-Based Interview Questions

1. A model has 99 percent accuracy but performs badly in production. What could be wrong with data split, leakage, imbalance, or metric choice?
2. A stakeholder asks why the model rejected a customer. How do you explain feature importance and limitations responsibly?
3. Training score is high but test score is low. Explain overfitting and fixes.
4. New data has missing values that training did not have. How should preprocessing and validation handle this?
5. A model is biased against one user group. What analysis and governance steps are needed?

## Portfolio Proof

By the end of this track, learners should publish:

- One architecture diagram.
- One working lab or project.
- Screenshots or command logs.
- A troubleshooting note.
- Five written interview answers using the format: problem, architecture, decision, tradeoff, security, monitoring, rollback.

## Official References

- https://scikit-learn.org/stable/getting_started.html
- https://docs.pytorch.org/tutorials/beginner/basics/intro.html
- https://www.tensorflow.org/guide
