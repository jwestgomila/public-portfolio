from abc import ABC, abstractmethod


class Classifier(ABC):
    def __init__(self):
        self.iterations = None
        self.learning_rate = None
    
    @abstractmethod
    def train(self, data):
        raise NotImplementedError("Method 'train' is not implemented")
        
    @abstractmethod
    def predict(self, data):
      raise NotImplementedError("Method 'predict' is not implemented")