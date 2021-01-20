# python高级特性

------

[TOC]

## 1.切片

截断

## 2.迭代

可迭代对象   就可以  for  in

```python
# 判断一个对象是不是可迭代对象
from collections import Iterable
isinstance("abc",Iterable)


可迭代对象  1. generator  2. tuple  list  set  dict  string
```



## 3.推导式

```python
1. 列表推导式结构:  
格式 : [ expression for variable in old_list]
       [expression for variable in old_list if condition]
# 列表
name = ['dasd','dsadasdas','tom','bob','jack']
name_ = [ item.title() for item in name if len(item)>3]
na =  filter(lambda item: len(item)>3 ,name)
# 元组 
tuple_ = [(i,j) for i in range(5)  if i%2==0 for j in range(11) if j%2!=0 ]
# 字典
list1 = ['zhangsan','lisi','wangwu','maliu',]
list3 = [1,2,3,4,]
list2 = { x : y for x,y in zip(list1,list3)}
```

## 4.生成器

```python
'''
通过列表生成式，我们可以直接创建一个列表。
但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，
那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器：generator。		
'''

generator = (x*2 for x in range(10))
# 通过 __next__() 魔术方法  得到下一个
# 通过 next(generator) 得到下一个
# 也可以  循环
print(generator.__next__())

print(next(generator))

for g in generator:
    print(g)
  
'''
    1. 定义一个函数  在函数中使用  yield 关键字
    2. 调用函数，接收调用的结果
    3. 得到的结果就是生成器
    4. next()   __next__   send() 函数在  generator 没有取过值的情况下  报错
'''

def func(length):
    n = 0;
    while n<length:
        n += 1
        yield n  # return n + 暂停
    return 'no more data'
g = func(3)
print(g)

print(next(g))
print(next(g))
print(next(g))
```

## 5.迭代器

可以被 next() 调用并不断 ，返回下一个值的对象称为  迭代器

**可迭代** 不一定是迭代器   可迭代对象 的可以通过内置函数 iter() 变成迭代器

 特点: 只能前进不能后退

可迭代对象  1. generator  2. tuple  list  set  dict  string