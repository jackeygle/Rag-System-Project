# Machine Learning Guide

## What is Machine Learning?

Machine Learning (ML) is a branch of artificial intelligence that enables computers to learn from data without being explicitly programmed. ML algorithms use historical data to make predictions or decisions.

## Main Types

### 1. Supervised Learning

Supervised learning uses labeled data to train models. Main tasks include:

- **Classification**: Predicting discrete labels, such as spam detection
- **Regression**: Predicting continuous values, such as house price prediction

Common algorithms:
- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forest
- Support Vector Machines (SVM)

### 2. Unsupervised Learning

Unsupervised learning works with unlabeled data, mainly used for:

- **Clustering**: Grouping similar data together
- **Dimensionality Reduction**: Reducing the number of features

Common algorithms:
- K-means Clustering
- Hierarchical Clustering
- Principal Component Analysis (PCA)

### 3. Reinforcement Learning

Reinforcement learning learns optimal strategies through interaction with the environment. The agent learns by trial and error to maximize cumulative rewards.

Applications:
- Game AI (e.g., AlphaGo)
- Robotics Control
- Autonomous Driving

## Deep Learning

Deep learning is a subset of machine learning that uses multi-layer neural networks to learn hierarchical representations of data.

### Common Architectures

1. **Convolutional Neural Networks (CNN)**: For image processing
2. **Recurrent Neural Networks (RNN)**: For sequential data
3. **Transformers**: For natural language processing
4. **Generative Adversarial Networks (GAN)**: For generating new data

## Gradient Descent

Gradient descent is the core algorithm for optimizing machine learning models. It iteratively adjusts model parameters to minimize the loss function.

### How It Works

1. Calculate the gradient of the loss function with respect to parameters
2. Update parameters in the opposite direction of the gradient
3. Repeat until convergence

### Variants

- **Batch Gradient Descent (Batch GD)**: Uses all data
- **Stochastic Gradient Descent (SGD)**: Uses one sample at a time
- **Mini-batch Gradient Descent**: Uses small batches of data

## Model Evaluation

### Classification Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- AUC-ROC

### Regression Metrics

- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- R² Score

## Overfitting and Underfitting

- **Overfitting**: Model performs well on training data but poorly on new data
- **Underfitting**: Model is too simple to capture data patterns

### Solutions

- Regularization (L1, L2)
- Dropout
- Early Stopping
- Data Augmentation
- Cross-validation
