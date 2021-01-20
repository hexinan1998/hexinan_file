# Python基础

------

[TOC]



## 1.数据类型与变量

### 1.1整数 int

```python
i = 1   # 1
i = 0x10 # 16  ox 开头为十六进制
```

### 1.2 浮点数 float

```python
f = 1.2  #1.2
f = 1.23e9 # 1.23 乘 10的 9 次方
```

### 1.3字符串

```python
str = "he"	# he
str = 'he'	# he
#  输出 " , ' , \  等字符要使用转义字符
str = 'he\"xi\\n\'an\"'  # he"xi\n'an"
#  r'' 保持字符串原样
str = r' \\\\\\sad''"""' #  \\\\\\sad"""
# 输出多行
str = ''' asdkjljaslkjd
sadjkljljsakld
asdjlakjld '''
# 形如这样  '''   ''' 无赋值表示多行 注释
'''
 asdkjljaslkjd
sadjkljljsakld
asdjlakjld
'''
```

### 1.4布尔值

```python
bool = True  # True
bool = False # False
```

### 1.5 空值

```python
# 空值不是 0 ，表示 变量指针没有指向的值 
a = None
```

### 1.6 常量

所谓常量就是不能变的变量，比如常用的数学常数" 派 "就是一个常量。在Python中，通常用全部大写的变量名表示常量。这只是一个约定 ，它本身还是可以变量，但是约定它不改动。

### 【注】

这种变量本身类型不固定的语言称之为*动态语言*，与之对应的是*静态语言*。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言

```python
# java
int a = 10
String str = "str"
# c
int a = 9
char str[] = "str"

# python
a = 10
a = "str"
```

## 2.字符串与编码

### 2.1 字符编码   ----  用数字代替文本

计算机只能存储数字，处理文本就得把文本变成数字。最早的计算机在设计时采用8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是`255（二进制11111111=十进制255）`，如果要表示更大的整数，就必须用更多的字节。比如两个字节可以表示的最大整数是`65535`，4个字节可以表示的最大整数是`4294967295`

由于计算机是美国人发明的，因此，最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为**`ASCII`编码**，比如大写字母`A`的编码是`65`，小写字母`z`的编码是`122`

但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和**ASCII编码**冲突，所以，中国制定了**`GB2312`编码**，用来把中文编进去。

全世界有上百种语言，日本把日文编到`Shift_JIS`里，韩国把韩文编到`Euc-kr`里，各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。

因此，**Unicode字符集**应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了

**Unicode标准**也在不断发展，但最常用的是**UCS-16编码**，用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode。

现在，捋一捋**ASCII编码**和**Unicode编码**的区别：**ASCII编码**是1个字节，而**Unicode编码**通常是2个字节。

```python
'''
字母A用 ASCII编码 是十进制的65，二进制的01000001；

字符0用 ASCII编码 是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；

汉字中已经超出了 ASCII编码 的范围，用 Unicode编码 是十进制的20013，二进制的01001110 00101101。

可以猜测，如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的 Unicode编码 是00000000 01000001。
'''
```

新的问题又出现了：如果统一成**Unicode编码**，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用**Unicode编码**比**ASCII编码**需要多一倍的存储空间，在存储和传输上就十分不划算。

所以，本着节约的精神，又出现了把**Unicode编码**转化为“可变长编码”的`UTF-8`编码。**UTF-8编码**把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用**UTF-8编码**就能节省空间：

| 字符 | ASCII    | Unicode           | UTF-8                      |
| ---- | -------- | ----------------- | -------------------------- |
| A    | 01000001 | 00000000 01000001 | 01000001                   |
| 中   | x        | 01001110 00101101 | 11100100 10111000 10101101 |

**在计算机内存中**，统一使用**Unicode编码**，当需要保存到硬盘或者需要传输的时候，就转换为**UTF-8编码**

用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：

![0](C:\Users\Hexinan_cp\Desktop\python\image\0.png)

浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：

![1](C:\Users\Hexinan_cp\Desktop\python\image\1.png)

### 2 .2Python的字符串

在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

```python
print('包含中文的str') # 包含中文的str

```

对于单个字符的编码，Python提供了`ord()`函数获取字符的整数表示，`chr()`函数把编码转换为对应的字符：

```python
ord('A') # 65
chr(66) # B
#  如果知道字符的整数编码，还可以用十六进制这么写str：   \u 表示 16 进制转移
str = '\u4e2d\u6587' # 中文
```

由于Python的字符串类型是`str`，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把`str`变为以字节为单位的`bytes`

以Unicode表示的`str`通过`encode()`方法可以编码为指定的`bytes`，例如

```python
 'ABC'.encode('ascii') # b'ABC'
 '中文'.encode('utf-8')  #  b'\xe4\xb8\xad\xe6\x96\x87'
```

纯英文的`str`可以用`ASCII`编码为`bytes`，内容是一样的，含有中文的`str`可以用`UTF-8`编码为`bytes`。含有中文的`str`无法用`ASCII`编码，因为中文编码的范围超过了`ASCII`编码的范围，Python会报错

在`bytes`中，无法显示为ASCII字符的字节，用`\x##`显示。

反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是`bytes`。要把`bytes`变为`str`，就需要用`decode()`方法

```python
b'ABC'.decode('ascii') # "ABC
len("abc") # 3
```



### 2.3 格式化

| 占位符 | 替换内容     |
| :----- | :----------- |
| %d     | 整数         |
| %f     | 浮点数       |
| %s     | 字符串       |
| %x     | 十六进制整数 |

```python
'''
经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串
%运算符 就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
'''
#1
print('%2d-%02d' % (3, 1))  # 3-01
print('%.2f' % 3.1415926)
print("{}")
#2
"my name is {} , {} years old".format("hexinan",18)
#3
name = hexinan
age = 18
print(f"my name is {name} , {age} years old")
```

## 3.list 和 tuple

list 列表   tuple 元组  （两者最大的区别就是  list 可变  tuple是不可变的）



### 3.1 list

```python
classmates  = ["zhangsan","lisi","wangwu"]
len(classmates)  # 3
classmates[0]  #  zhangsan
# z最后一个元素可以使用  -1  作为索引
# 可迭代，可更改 ，内含元素类型不必单一 ， 支持多种数据（包括自定义），
# 支持切片
classmates_man = classmates[1:]  # ['lisi', 'wangwu']

# 功能性特征
# 增 
classmates.append("maliu") # ['zhangsan', 'lisi', 'wangwu', 'maliu']

# 删
classmates.pop() # ['zhangsan', 'lisi', 'wangwu']  并且 返回删除元素 
classmates.pop(1) # 删除指定位置元素  ['zhangsan', 'wangwu']  并且 返回删除元素 

# 改
classmates[0] = "hexinan" #['hexinan', 'wangwu']

# 查  可迭代 立即推 可以使用循环

# 排

# 插
classmates.insert(1,"lisi") # ['hexinan', 'lisi', 'wangwu']

```

### 3.2 tuple

```python
# 这个 数据 类型与 list 很相似 除了不可修改所有的 特性都一样
# 也就是说  与 list 的 distinction 就是   一旦定义就不可以修改 

# append 不可用    insert不可用

t = ("a","b",["c","d"])
t[2][1] = "2"
print(t) # ('a', 'b', ['c', '2'])
# 这个例子要理清 指针指向 tuple 不变，包含 list 改变
```

## 4.流程控制

```python
if age > 0 and age < 18:
    pass
elif age > 18 or father != "hexinan":
    pass
else:
    pass


for A in B:
    pass
# B 此时必须是一个 可迭代的 数据类型
break #  破坏整层循环
continue # 破坏单层循环
    
    
while n > 1:
    pass
```

## 5.使用dict和set

```python
'''
dict
'''

d = {"zhangsan":17 , "lisi":18 , "wangwu":19}
d["zhangsan"] # 17 

# 增
d["hexinan"] = 18

# 删
d.pop("lisi")

# 改
d["wangwu"] = 18

# 查 可迭代
len(d)
d.keys()
d.values()
d.items()
d.get("wangwu") # return value
"KEY" in d # return bool


'''
set
与  dict 相似。 只是内容不会重复，且只保存 key
'''

add(key)
remove(key)
```



