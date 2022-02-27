import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def loadData():
    with np.load('notMNIST.npz') as dataset:
        Data, Target = dataset['images'], dataset['labels']
        posClass = 2
        negClass = 9
        dataIndx = (Target==posClass) + (Target==negClass)
        Data = Data[dataIndx]/255.
        Target = Target[dataIndx].reshape(-1, 1)
        Target[Target==posClass] = 1
        Target[Target==negClass] = 0
        np.random.seed(421)
        randIndx = np.arange(len(Data))
        np.random.shuffle(randIndx)
        Data, Target = Data[randIndx], Target[randIndx]
        trainData, trainTarget = Data[:3500], Target[:3500]
        validData, validTarget = Data[3500:3600], Target[3500:3600]
        testData, testTarget = Data[3600:], Target[3600:]
    return trainData, validData, testData, trainTarget, validTarget, testTarget



def loss(w, b, x, y, reg):
    # Your implementation here
    y_hat = np.matmul(x, w) + b

    err = np.square(y_hat - y)
    loss_mse = np.sum(err) / (2 * len(y))
    loss_reg = (np.linalg.norm(w) ** 2) * reg / 2
    return loss_mse + loss_reg

def grad_loss(w, b, x, y, reg):
    # Your implementation here
    return 0
def grad_descent(w, b, x, y, alpha, epochs, reg, error_tol):
    # Your implementation here
    return 0
