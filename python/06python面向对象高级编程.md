# 面向对象高级编程

------

[TOC]

## 使用     `__slots__`

```python
class Student(object):
    pass

s = Student()
s.name = "hexin"
print(s.name) # hexin

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
from types import MethodType

s.set_age = MethodType(set_age,s) #给实例绑定一个方法
s.set_age(25)
s.age # 测试结果   25
#  这样虽然给一个  实例绑定了方法 ， 但是对另一个实例却不起作用
#  为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score

Student.set_score() = set_score

'''
但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
'''

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

```

## 使用@property

```python
# 在 直接使用 obj.attribute  使用和修改的前提下 ，  增加 数据检测或其他操作 的方法
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
# @property 广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，
# 这样，程序运行时就减少了出错的可能性。

```

## 多重继承 

```python
'''
多继承
    class A:
        pass
    class B:
        pass
    class C(A,B):
        pass
        
现在执行环境python3   新式类
经典类： 深度优先搜索
新式类： 广度优先搜索

'''
class Base:
    def test(self):
        print("base  base   base")


class A(Base):
    def test(self):
        print("AAAAA")


class B(Base):
    def test(self):
        print("BBBBBBB")


class C(Base):
    def test(self):
        print("CCCCCC")

class D(A,B,C):
    pass

import inspect
print(inspect.getmro(D))


d = D()
d.test()

print(D.__mro__) 
```

**MixIn**

在设计类的继承关系时，通常，主线都是单一继承下来的，例如，`Ostrich`继承自`Bird`。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让`Ostrich`除了继承自`Bird`外，再同时继承`Runnable`。这种设计通常称之为 MixIn

## 魔术方法

```python
'''
-------------------普通方法是 写了必须调用  而 魔术方法  你写了它会自动触发 ，调用。

__init__ : 初始化魔术方法                 ********************************
触发时机： 初始化对象时触发（不是实例化触发，而是和实例化在一个操作中）

__new__ : 实例化对象魔术方法   **基本不会重写
触发时机： 构造实例化对象时出发（ 开辟内存部分）

构造实例化并初始化过程 ：
    --->  __new__ 划分内存并返回地址 
    --->  __init__  self 接到地址 并进行 初始化赋值。
    --->  返回地址 交给 实例化对象

__call__: 调用对象的魔术方法   ****取决自己想不想
触发时机： 当对象被当作函数执行时触发

__del__: delete的缩写 ， 析构魔术方法   **%99   不会重写
触发时机： 当对象没有用的时被触发  
1.对象赋值
2.删除地址的引用 del p1 
3.查看地址引用的次数   sys.getrefcount(p) 
4.对象 （所有的引用）都没有时
5.  当空间没有因用之后    python 解释器 （执行垃圾回收） 释放内存 （调用 del ) 

__str__: tostring() 方法  （给用户看的）   ************************************
触发机制：当打印对象名时

__iter__:	该方法返回一个迭代对象
触发时机：如果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，
Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。

__getattr__： 固定传入  slef , attribute
触发时机:调用不存在属性时


'''

import sys

class Person:

    def __init__(self,name):
        self.name = name

    def __new__(cls,*arg,**kwarg):
        print("ccc")
        return super().__new__(cls)

    def __call__(self, *args, **kwargs):
        print("__call 被执行了__")

    def __del__(self):
        print("__del 被执行了__")

    def __str__(self):
        return "这是要打印的值"

p1 = Person("hexinan")
p2 = p1

print(sys.getrefcount(p1))

del p2

print("111")
print(p1.name)
p1()

print(p1)
```

## 使用枚举类

```python
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
    
    
'''
value属性则是自动赋给成员的int常量，默认从1开始计数。
如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
'''
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# 使用方式如下
Weekday.Mon # Weekday.Mon
Weekday['Tue'] # Weekday.Tue
Weekday.Tue.value # 2
Weekday(1) # Weekday.Mon
```

## 使用元类

```python
from hello import Hello
h = Hello()
h.hello() # Hello, world.
print(type(Hello))# <class 'type'>
print(type(h)) # <class 'hello.Hello'>

'''
type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。

我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
'''
'''

要创建一个class对象，type()函数依次传入3个参数：

class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上

通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
'''
```

**metaclass**

当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例

但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类

metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到



