import numpy as np

a = np.array([1, 23, 4], dtype=np.int64)  # dtype 中 int64 , float64

b = np.zeros((3, 4), dtype = np.int64  )# ones()  zeros empty

c = np.empty((3, 4))

print(a)
print(b)
print(c)

# 生成一个  (3, 4) 的矩阵
d = np.arange(12).reshape((3, 4))
print(d)

#  linespce 将  start 与 end  分为20份，调用  shape 将其直接转换为  4，5 矩阵
e = np.linspace(1, 10, 6).reshape((2, 3))
print(e)