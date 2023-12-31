# coding: utf-8
import numpy as np


# 恒等函数
def identity_function(x):
    return x


# 阶跃函数
def step_function(x):
    return np.array(x > 0, dtype=np.int)


# sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_grad(x):
    return (1.0 - sigmoid(x)) * sigmoid(x)


# 修正线型函数
def relu(x):
    return np.maximum(0, x)


def relu_grad(x):
    grad = np.zeros_like(x)
    grad[x >= 0] = 1
    return grad


# softmax函数
def softmax(x):
    x = x - np.max(x, axis=-1, keepdims=True)  # 溢出对策
    return np.exp(x) / np.sum(np.exp(x), axis=-1, keepdims=True)


# 均方误差
def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)


# mini-batch版交叉熵误差
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 如果教师数据是独热编码（one-hot-vector）的情况下，将其转换为正确标签的索引
    if t.size == y.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


def softmax_loss(X, t):
    y = softmax(X)
    return cross_entropy_error(y, t)
