#!/usr/bin/python
# encoding utf-8
"""
@author: jing
@time:  Created on 2017/4/1017:31
@file LogisticRegression.py
@desc
"""
import logging
import numpy as np

class LogisticRegressionClassifier():

    def __init__(self):
        print('create logisticRegressionClassifier')
        pass

    #定义一个sigmoid
    def _sigmoid(self, fx):
        return 1.0/(1+np.exp(-fx))

    def loss(self, W, X, y,  reg=1e-5):
        pass

    def _gradDescent(self,X, y, W=None,learning_rate=1e-3, num_iters=100):
        X = np.mat(X)
        y = np.mat(y).transpose()
        num_train, dim = X.shape
        num_classes = np.max(y) + 1  # assume y takes values 0...K-1 where K is number of classes

        if W is None:
            W = 0.001 * np.random.randn(dim, 1)
        #本算法参考http://blog.csdn.net/dongtingzhizi/article/details/15962797
        for it in range(num_iters):
            h = self._sigmoid(X*W)
            error = (y - h)
            W = W + learning_rate * X.transpose()*error
        print('W:',W.shape)
        return W

    def train(self, X, y, W=None,learning_rate=1e-3, num_iters=100):
        return self._gradDescent(X, y, W=None,learning_rate=1e-3, num_iters=100)


    def predict(self, X, y, W):
        X = np.mat(X)
        y = np.mat(y).transpose()
        y_pred = np.zeros(X.shape[1])
        print('X_predict', X.shape)
        print('y:',y.shape)
        print('w:', W.shape)
        hx = self._sigmoid(X*W)
        m = len(hx)
        error = 0.0
        for i in range(m):
            if int(hx[i]) >0.5:
                print(str(i+1)+'-th sample', int(y[i]),'is classified as :1')
                if int(y[i]!=1):
                    error += 1.0
                    print('classify error.')
            else:
                print(str(i+1)+'-th sample', int(y[i]),'is classified as :1')
                if int(y[i] != 0):
                    error += 1.0
                    print('classify error.')
        error_rate = error / m
        print('error rate is:%.4f',error_rate)
        return error_rate



