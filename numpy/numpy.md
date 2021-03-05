# numpy

------

[TOC]

## 1. 基本使用的结构

此部分慢慢补充

```python
# array 创建

np.array()
np.zeros()
np.one()
np.empty()
np.full()
np.eye()
np.arange()
np.linspace()
np.logspace()
np.diag()
np.tri()
np.vander() #  范德蒙行列式

# array 属性

array = np.array([[1,2,3],[4,5,6].[7,8,9]])
array.shape
array.size
array.T
array.real
array.imag

# array 操作

array.copy()  # 只有copy才会 重新开空间复制值
array.reshape() # copy 返回 新的大小 数组 
array.resize() # 直接改变原数组的值
array.flatten() # 拉成一维
array.sort() 
array.max()
array.min()
array.ptp()
array.sum()
array.round()
array.mean()
array.var()
array.std()
array.prod()
array.all()
array.any()

# array 索引
1. 切片	array[1:3,1:3]
2. 键对索引  
	array[[0,2],[1,3]] 得到的值是 (0,1)  (2,3)
3. np.ix_ 
	array[np.ix_([0,2],[1,3])]
4. np.nditer  迭代器 for loop
	
# np 的操作 (数组的拼接与拆分)

hstack(array1,array2) # 水平向  增加
vstack # 垂直向  增加
stack  # 0 维度  增加
hsplit(array1,2) #水平向  切  
vsplit # 垂直向  切  
split  # 第一维度 切

1.三角函数   2.数学计算    3.财务统计  4.统计   5.数组屏蔽
```

## 2.数组的创建

```python
# array 创建

np.array()
def array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0)
#Create an array.

np.zeros()
def zeros(shape, dtype=float, order='C')
#Return a new array of given shape and type, filled with zeros.

np.one()
def zeros(shape, dtype=float, order='C')
#Return a new array of given shape and type, filled with zeros.

np.empty()
def empty(shape, dtype=float, order='C')
#Return a new array of given shape and type, without initializing entries.

np.eye()

def eye(N, M=None, k=0, dtype=float, order='C')
#Return a 2-D array with ones on the diagonal and zeros elsewhere.

np.arange()
def arange(start=None, stop, step=None, , dtype=None)
#Return evenly spaced values within a given interval

np.linspace()
def linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
#Return evenly spaced numbers over a specified interval
np.logspace()

np.diag()
np.tri()
np.vander()
```

