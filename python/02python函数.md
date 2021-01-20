# python函数

------

[TOC]

## 1.调用函数

函数名（参数）

```python
funtion(arg, )
```



## 2.定义函数

```python
def funtion(arg1,arg2):
    operate
    return result
```

## 3.函数参数

```python
'''
位置参数   默认参数  可变参数   关键字参数  命名关键字参数（使用特殊分割符 *）
'''
def fun(name,age=18,*arg1,**arg2):
    pass

def fun(name,age,*,city,job):
    pass

#顺序必须如下
	必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
```



