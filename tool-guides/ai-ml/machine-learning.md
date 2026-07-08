# Machine Learning Guide

![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

## What It Is

Machine learning teaches computers to make predictions or decisions from data. The learner focus is data preparation, feature engineering, model training, evaluation, interpretation, and limitations.

## Core Workflow

```text
Data -> cleaning -> feature engineering -> train/test split -> model training -> evaluation -> explanation -> saved artifact
```

## Learn In This Order

1. Python, NumPy, Pandas, and basic statistics.
2. Supervised learning: classification and regression.
3. Unsupervised learning: clustering and dimensionality reduction.
4. Train/test split, cross-validation, and leakage prevention.
5. Metrics: accuracy, precision, recall, F1, ROC-AUC, MAE, RMSE.
6. Pipelines and preprocessing.
7. Hyperparameter search.
8. Model interpretation and model cards.
9. Deep learning basics with PyTorch or TensorFlow after ML fundamentals are clear.

## Practical Architecture

```text
Notebook/script -> dataset -> preprocessing pipeline -> estimator -> metrics -> model file -> model card
```

## Common Tools

- Scikit-learn for classical ML.
- Pandas and NumPy for data work.
- Matplotlib or similar tools for visualization.
- PyTorch/TensorFlow for deep learning.
- MLflow for experiment tracking when moving toward MLOps.

## Scenario Interview Questions

1. Accuracy is high but business results are poor. Which metric and data issues do you check?
2. Training score is excellent and test score is weak. Explain overfitting and fixes.
3. A feature leaks future information. How do you detect and prevent leakage?
4. A model treats one group unfairly. How do you investigate bias and document limits?
5. A stakeholder asks why the model made a prediction. What explanation methods and caveats do you provide?

## Official References

- https://scikit-learn.org/stable/getting_started.html
- https://docs.pytorch.org/tutorials/beginner/basics/intro.html
- https://www.tensorflow.org/guide
