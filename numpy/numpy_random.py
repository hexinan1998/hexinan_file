import numpy as np

# 随机生成矩阵  值在  0-1 直接
a = np.random.random((2, 4))

print(a)
print(np.sum(a))
print(np.min(a, axis=1))
print(np.max(a))

a  = np.arange(2, 14).reshape(3, 4)
print(a)

# 打印它最大的索引
# 打印它最小的索引

print(np.argmin(a))
print(np.argmax(a))

# 打印 平均值
print(np.average(a))
# 打印 中位数
print(np.median(a))
# 累加
print(np.cumsum(a))  # 之前的的数差值
# 累差
print(np.diff(a))
# 找出 不是 0 的数
print(np.nonzero(a))
# 排序
a = np.arange(14, 2, -1).reshape((3, 4))
print(a)
print(np.sort(a))
# 矩阵的转置
print(np.transpose(a))
print((a.T).dot(a))

print()

