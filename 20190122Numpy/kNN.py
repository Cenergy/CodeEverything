# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '23/1/2019 4:48 PM'

import numpy as np
from math import sqrt
from collections import Counter


class kNNClassify:
    def __init__(self, k):
        assert k >= 1, "k must be vaild"
        self.k = k
        self._X_train = None
        self._y_train = None

    def fit(self, X_train, y_train):
        self._X_train = X_train
        self._y_train = y_train
        return self

    def predict(self, X_predict):
        assert self._y_train is not None and self._X_train is not None, "must fit before predict"
        y_predict = [self._predict(x) for x in X_predict]
        return np.array(y_predict)

    def _predict(self, x):
        distance = [sqrt(np.sum((x_train - x) ** 2)) for x_train in self._X_train]
        nearest = np.argsort(distance)
        topK_y = [self._y_train[i] for i in nearest[:self.k]]
        votes = Counter(topK_y)
        predict_y = votes.most_common(1)[0][0]
        return predict_y

    def __repr__(self):
        return "KNN(k=%d)" % self.k


if __name__ == '__main__':
    a = [[3.393533211, 2.331273381],
         [3.110073483, 1.781539638],
         [1.343808831, 3.368360954],
         [3.582294042, 4.67917911],
         [2.280362439, 2.866990263],
         [7.423436942, 4.696522875],
         [5.745051997, 3.533989803],
         [9.172168622, 2.511101045],
         [7.792783481, 3.424088941],
         [7.939820817, 0.791637231]]
    raw_data_X = np.array(a)
    y_train = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
    x = np.array([8.093607318, 3.365731514]).reshape(1,-1)
    knn=kNNClassify(k=6)
    knn.fit(raw_data_X,y_train)
    print(knn.predict(x))
