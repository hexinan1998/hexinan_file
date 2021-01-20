# 面向对象编程

------

[TOC]

## 类和实例

类的方法

初始化方法

```python
class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
stu1 = Student("hexinan",100)
```

**数据封装** 

这样一来，我们从外部看`Student`类，就只需要知道，创建实例需要给出`name`和`score`，而如何打印，都是在`Student`类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。

## 访问权限

以把属性的名称前加上两个下划线`__`，在Python中，实例的变量名如果以`__`开头，就变成了一个**私有变量**（private）

这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，**代码更加健壮**。

外部代码要**获取**name和score 可以给Student类增加`get_name`和`get_score`这样的方法

外部代码要**修改**score 可以给Student类增加set_score这样的方法

```python
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        self.__score = score
```

你也许会问，原先那种直接通过`bart.score = 99`也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数

## 继承与多态

```python
'''
1.类关系
has a ---- A has a B 表示 A 包含 B，从属关系 ，人有名字  类中使用 其他对象作为属性
is a  -----A is a B  表示 A 是 B ，继承关系， 服务器是计算机  ， 工作站也是计算机
类型
    系统类型
        str int ....
    自定义类型
        class  定义的

2.继承   is a  （基类,父类，超类）

    student, employee ,doctor  都属于人类
    都有很多相同的代码
    提取相同的部分 创建底层类
 继承的特点
    1. 如果类中没有 __init__ 调用父类的 __init__方法
    2. 如果继承父类  也需要定义自己的  __init__,就需要在子类的 __init__ 调用   父类 __init__
    3. 通过 super().__init__([args])
            super(类名，对象).__init__([args])
    4. 方法 寻找   ---从当前类，--- 父类。

***** 父类一些私有的属性是不能继承的  在方法中也是不能访问***

'''
```



```python
class Animal(object):
    def run(self):
        print('Animal is running...')
# 继承
class Dog(Animal):
    pass

class Cat(Animal):
    pass


# 多态
'''
按字面的意思就是“多种状态”。在面向对象语言中，接口的多种不同的实现方式即为多态
多态性是允许你将父对象设置成为一个或更多的他的子对象相等的技术

'''
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

isinstance(b, Animal)
isinstance(c, Dog)
isinstance(c, Animal)
```

![image-20210119220030075](C:\Users\Hexinan_cp\AppData\Roaming\Typora\typora-user-images\image-20210119220030075.png) 

**静态语言 vs 动态语言**

对于静态语言（例如Java）来说，如果需要传入`Animal`类型，则传入的对象必须是`Animal`类型或者它的子类，否则，将无法调用`run()`方法。

对于Python这样的动态语言来说，则不一定需要传入`Animal`类型。我们只需要保证传入的对象有一个`run()`方法就可以了

这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个`read()`方法，返回其内容。但是，许多对象，只要有`read()`方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了`read()`方法的对象

## 获取对象信息

**type()**

**isinstance()**

**dir()**

## 实例属性和类属性

```python
class Student(object):
    school = 'qh'
    def __init__(self, name):
        self.name = name

s = Student('Bob')

# 实例属性
s.score = 90
# 类属性
print(s.school)
```

