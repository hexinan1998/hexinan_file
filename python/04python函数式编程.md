# python函数式编程

------

[TOC]

## 1.高阶函数

### 1.1定义

```python
1. 函数本身可以赋值给变量，赋值后变量为函数
2. 允许将函数本身作为参数传入
3. 允许返回一个函数
# 1
def fun():
	print("hello world")
fun1 = fun
fun1() # hello world

# 2
def fun2(f):
    f()
fun2(fun) # hello world
```

### 1.2 map / reduce

```python
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

reduce() 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce

```

### 1.3 filter

```
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

```



### 1.4 sorted

```
sorted()函数就可以对list进行排序
可以传入一个映射函数  key  让其实现排序
sorted()排序的关键在于实现一个映射函数。
```

### 1.5 max() /min()

## 2.返回函数

函数作为返回值

闭包-----是实现装饰器的原理

闭包作用就是   保存内部变量供外部环境访问

## 3.匿名函数

```python
lambda x: x * x
'''
相当与
'''
def fun(x):
    return x*x
```



## 4.装饰器

```python

islogin = False

#定义一个装饰器   ， 进行付款验证

def  login():
    username = input("输入用户名：")
    password = input("输入密码：")
    if username == 'admin' and password == '1234':
        return True
    else:
        return False

def login_required(func):
    
    def wrapper(*args,**kwargs):
        global islogin
        #验证用户是否登陆
        if islogin:
            func(*args,**kwargs)
        else:
            print("用户没有登陆，不能付款")
            islogin = login()
    return wrapper



@login_required
def pay(money):
    print(f"付款金额是{money}")
    print("正在付款")
    print("付款成功！")

pay(200)
pay(1000)
```

## 5.偏函数

很少用