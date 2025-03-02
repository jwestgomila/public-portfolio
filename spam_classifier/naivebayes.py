import math
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from classifier import Classifier


class NaiveBayesSpamClassifier(Classifier, BaseEstimator, ClassifierMixin):
    name = "Naive Bayes"
    
    def __init__(self):
        Classifier.__init__(self)
        self.log_class_priors = None
        self.log_class_conditional_likelihoods = None
        
    def train(self, data):
        self.log_class_priors = self.estimate_log_class_priors(data)
        self.log_class_conditional_likelihoods = self.estimate_log_class_conditional_likelihoods(data)
        
    def predict(self, data):
      class_predictions = np.array([-1] * len(data))
      for i in range(len(data)):
          row = data[i]
          prob_ham = self.log_class_priors[0] + np.dot(row, self.log_class_conditional_likelihoods[0])
          prob_spam = self.log_class_priors[1] + np.dot(row, self.log_class_conditional_likelihoods[1])
          class_predictions[i] = 0 if prob_ham > prob_spam else 1
      return class_predictions
    
    def fit(self, X, y):
        self.classes_ = np.unique(y)
        data = np.hstack((y.reshape(-1, 1), X))
        self.train(data)
        return self
  
    def score(self, X, y):
        predictions = self.predict(X)
        return np.mean(predictions == y)
    
    def estimate_log_class_priors(self, data):
      class_priors = [0, 0]
      for row in data:
          class_prior = row[0]
          if class_prior == 0:
              class_priors[0] += 1
          else:
              class_priors[1] += 1

      for i in range(len(class_priors)):
          prior = class_priors[i]
          class_priors[i] = math.log(prior / len(data))

      return np.array(class_priors)
    
    def estimate_log_class_conditional_likelihoods(self, data):
      spam_mask = (data[:, 0] == 1)
      ham_mask = (data[:, 0] == 0)

      spam_data = data[spam_mask][:, 1:]
      ham_data = data[ham_mask][:, 1:]

      spam = np.sum(spam_data, axis=0)
      ham = np.sum(ham_data, axis=0)

      return np.array([NaiveBayesSpamClassifier.get_conditional_likelihood(ham), NaiveBayesSpamClassifier.get_conditional_likelihood(spam)])
    
    @staticmethod
    def get_conditional_likelihood(counts):
      total = np.sum(counts)
      return np.array([math.log((x + 2) / (total + (2 * len(counts)))) for x in counts])
