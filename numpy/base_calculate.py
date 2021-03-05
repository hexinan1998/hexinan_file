import numpy as np

a = np.array([10, 20, 30, 40])
print(a)
b = np.arange(4)

c = a+b
print(c)

d = a-b
print(d)

e = b**2
print(e)

#  sin   cos  tan
c = 10*np.sin(a)
print(c)

#  条件
print(b>2)

# 矩阵
matrix_1 = np.array([[1, 1], [0, 1]])
matrix_2 = np.arange(4).reshape((2,2))

print(matrix_1)
print(matrix_2)
# 逐个相乘
ma_ = matrix_1 * matrix_2
print("逐个相乘")
print(ma_)
# 矩阵相乘
ma_ = np.dot(matrix_1, matrix_2)
print("矩阵相乘")
print(ma_)
# 换一种表达
ma_ = matrix_1.dot(matrix_2)
print(ma_)
