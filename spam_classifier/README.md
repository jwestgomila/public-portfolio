These basic spam classifiers were made as part of a University of Bath Artificial Intelligence MSc assignment.

logistic_regression.py has the most complete implementation and it implements gradient descent on the squared error loss of the sigmoid predictions, along with elastic net regularisation. It achieved an accuracy of 93% and an F1 score of 89% on the provided test corpus.

I've included some figures that help support that claim and demonstrate the cross validation process used to tune the model.