import numpy as np

#  索引
a = np.arange(3, 15).reshape(3, 4)

# print(a)

# 可以对 行列  进行切片
print(a[2][1])
print(a[2, 1])
print(a[1, :])
print(a[:, 1])
print("-----分割线")
# 迭代行
for row in a:
    print(row)
print("-----分割线")
# 迭代列
for column in a.T:
    print(column)
# 迭代每一项
print(a.flatten())
for item in a.flat:
    print(item)

# 合并
a = np.array([1, 1, 1])
b = np.array([2, 2, 2])
c = np.vstack((a, b))  # vertical stack
d = np.hstack((a,b)) # horizontal stack



print("垂直")
print(c.shape)
print("水平")
print(d.shape)

#  单横列转竖列
print(a[:, np.newaxis])

np.concatenate((a, b), axis=0)
# 纵向合并  axis = 0  ，横向合并 axis = 1

#分割  分割成不同的  array

a = np.arange(12).reshape((3, 4))
print(a)

# print(np.split(a, 2, axis=1))
print(np.vsplit(a, 3))  # 从垂直方向切割

print(np.hsplit(a, 2))  # 从水平方向切割

#  赋值 array 对象赋值属于引用赋值
#   b = a.copy()　# deep copy




