#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: Jing 
@contact: 
@site:  
@software: PyCharm 
@file: knn.py 
@time: 2017/4/11 16:29 
"""

import numpy as np


class KNNClassifier(object):

    def __init__(self):
        pass

    def train(self, X, y):
        self.X_train = X
        self.y_train = y
        pass
    def predict(self, X, k=1):
        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        dists = np.sqrt(-2 * np.dot(X, self.X_train.T) + np.sum(np.square(self.X_train), axis=1) + np.transpose(
            [np.sum(np.square(X), axis=1)]))
        return self.predict_labels(dists, k=k)

    def predict_labels(self,dists, k = 1):
        num_test = dists.shape[0]
        y_pred = np.zeros(num_test)
        for i in range(num_test):
            closest_y = []
            closest_y = self.y_train[np.argsort(dists[i])[:k]]
            y_pred[i] = np.argmax(np.bincount(closest_y))
        return y_pred



