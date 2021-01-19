# np.meshgrid 用法：https://www.cnblogs.com/shanlizi/p/9127878.html
import numpy as np

a = np.array([2, 3])
b = np.array([4, 5])
A, B = np.meshgrid(a, b)
print(A * B)