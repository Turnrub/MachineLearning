## 基于knn的手写识别数字分析

### 1.数据认识
    1.手写数字的数据是一列0和1组成的列向量，存放在一个txt文件中；
### 2.数据的读取
    1.需要遍历data/trainingDitits目录下的所有文件；
    2.根据每个文件建立一个列向量；
    3.将向量组成一个矩阵；
    4.将文件名设为标签组成一个矩阵。
### 3.训练算法
    1.将X，y传入算法；
    2.训练。
### 4.算法中的不懂问题
    1.关于矩阵运算dists = np.sqrt(-2 * np.dot(X, self.X_train.T) + np.sum(np.square(self.X_train), axis=1) + np.transpose(
            [np.sum(np.square(X), axis=1)]))，不懂定理
            但与此有关：dists[i] = np.sqrt(np.sum(np.square(self.X_train - X[i]), axis = 1))

