import math
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from classifier import Classifier


class LogisticRegressionSpamClassifier(Classifier, BaseEstimator, ClassifierMixin):
    name = "Logistic Regression"
    
    def __init__(self, iterations=1000, learning_rate=0.1, lambda_l1=0.0001, lambda_l2=0.0001):
        super().__init__()
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.weights = None
        self.lambda_l1 = lambda_l1
        self.lambda_l2 = lambda_l2
        
    def train(self, data):
        y = data[:, :1]
        self.weights = np.zeros(data[:, 1:].shape[1]) * 1e9
        transposed = data[:, 1:].transpose()
        
        for i in range(self.iterations):      
          x_weights = np.matmul(self.weights, transposed)
          predictions = np.array([self.sigmoid(x) for x in x_weights])
          gradient = [np.mean(t) for t in -(y.flatten() - predictions) * predictions * (1 - predictions) * transposed]
          gradient_l1 = self.lambda_l1 * np.sign(self.weights)
          gradient_l2 = self.lambda_l2 * self.weights
          self.weights = self.weights - self.learning_rate * (gradient + gradient_l1 + gradient_l2)
        
    def predict(self, data):
      x_weights = np.matmul(self.weights, data.transpose())
      class_predictions = [1 if x > 0.5 else 0 for x in np.array([self.sigmoid(x) for x in x_weights])]
      return class_predictions
  
    def fit(self, X, y):
        self.classes_ = np.unique(y)
        data = np.hstack((y.reshape(-1, 1), X))
        self.train(data)
        return self
  
    def score(self, X, y):
        predictions = self.predict(X)
        return np.mean(predictions == y)
    
    def sigmoid(self, x):
        if x < 0:
            return math.exp(x) / (1 + math.exp(x))
        else:
            return 1 / (1 + math.exp(-x))
