import numpy as np
import matplotlib.pyplot as plt
from logistic_regression import LogisticRegressionSpamClassifier


class LogisticRegressionZipfianSpamClassifier(LogisticRegressionSpamClassifier):
    name = "Logistic Regression Zipfian"
    
    def __init__(self, iterations=1000, learning_rate=0.1):
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.weights = None
        
    def train(self, data):
        y = data[:, :1]
        features = data[:, 1:]
        self.weights = np.zeros(features.shape[1])
        transposed = features.transpose()
        weights = self.get_zipfian_weights(data)
        
        for i in range(self.iterations):      
          x_weights = np.matmul(self.weights * weights, transposed)
          predictions = np.array([self.sigmoid(x) for x in x_weights])
          self.weights = self.weights + [np.mean(t) for t in self.learning_rate * (y.flatten() - predictions) * predictions * (1 - predictions) * transposed]
    
    def get_zipfian_weights(self, data, i=1):
        spam_mask = (data[:, 0] == 1)
        spam_data = data[spam_mask][:, 1:]
        spam_feature_freq = np.sum(spam_data, axis=0)
        sorted_indices = np.argsort(spam_feature_freq)[::-1]
        ranks = np.empty_like(sorted_indices)
        ranks[sorted_indices] = np.arange(1, len(spam_feature_freq) + 1)
        return 1 / np.log(ranks + 1)

    def plot(self, ranks, spam_feature_freq):
        plt.figure(figsize=(8,6))
        plt.plot(ranks, spam_feature_freq, marker=".", linestyle="none")
        plt.xlabel("Rank")
        plt.ylabel("Frequency")
        plt.title("Zipfian Distribution of Email Features")
        plt.show()
    