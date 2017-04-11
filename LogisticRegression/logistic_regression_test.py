#!/usr/bin/python
# encoding utf-8
"""
@author: jing
@time:  Created on 2017/4/1110:36
@file logistic_regression_test.py
@desc
"""
import numpy as np


#每行数据以\t隔开，最后一列为类标号
from LogisticRegression.logistic_regression import LogisticRegressionClassifier


def loadDataSet(datafile):
    featData = []; labelDate = []
    with open(datafile, 'r') as fr_file:
        for eachline in fr_file:
            oneline = eachline.split('\t')
            tempArr = []
            for i in range(len(oneline)-1):
                tempArr.append(float(oneline[i]))
            featData.append(tempArr)
            labelDate.append(int(float(oneline[-1].strip())))
    return featData, labelDate   #返回的数据是list

def main():
    trainfile = r"data\train.txt"
    testfile = r"data\test.txt"
    train_X, train_y = loadDataSet(trainfile)
    test_X, test_y = loadDataSet(testfile)
    print(len(test_X), len(test_y))
    print('len(test_X), len(test_y)')
    clf = LogisticRegressionClassifier()

    weigh = clf.train(train_X, train_y, W=None, learning_rate=0.01, num_iters=500)

    clf.predict(test_X, test_y, weigh)

#主函数
if __name__=="__main__":
    main()


