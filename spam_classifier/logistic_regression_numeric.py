import numpy as np
from logistic_regression import LogisticRegressionSpamClassifier


class LogisticRegressionNumericSpamClassifier(LogisticRegressionSpamClassifier):
    name = "Logistic Regression Numeric"

    def train(self, data):
        labels = [x[0] for x in data[:, :1]]
        transposed = data[:, 1:].transpose()
        self.weights = np.zeros(data[:, 1:].shape[1])
        
        for i in range(self.iterations):
            h = 1e-5
            gradient = np.zeros_like(self.weights)
            for j in range(len(self.weights)):
                
                self.weights[j] += h
                x_dot_weights_plus = np.matmul(self.weights, transposed)
                predictions_plus = np.array([self.sigmoid(x) for x in x_dot_weights_plus])
                loss_plus = (labels - predictions_plus)**2
                self.weights[j] -= h
                
                self.weights[j] -= h
                x_dot_weights_minus = np.matmul(self.weights, transposed)
                predictions_minus = np.array([self.sigmoid(x) for x in x_dot_weights_minus])
                loss_minus = (labels - predictions_minus)**2
                self.weights[j] += h
                     
                gradient[j] = np.mean(loss_plus - loss_minus) / (2 * h)
            self.weights -= self.learning_rate * gradient
    