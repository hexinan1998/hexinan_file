import numpy as np

# 生成单位矩阵
e4 = np.eye(4)
print(e4)
# 添加矩阵
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array)
print(dir(array))

#打印矩阵维度  dimension
print("number of dim:", array.ndim)
#打印形状
print("shape:", array.shape)

#打印所有的元素
print("size", array.size)





