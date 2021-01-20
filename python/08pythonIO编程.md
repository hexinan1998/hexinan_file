# IO编程

------

[TOC]



## 1.文件读写

```python
f = open('/Users/michael/test.txt', 'r') #  路径  文件权限
# 如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在

f.read() # read()  方法一次性全部读取文件  Python把内容读到内存，用一个str对象表示
f.close() #文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的


#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
#所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
#但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法

with open('/path/to/file', 'r') as f:
    print(f.read())

'''   
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
'''
'''

文件
文件操作：
    open()  path filename
    mode   r w rb wb a

    stream = open()
    stream.read()
    stream.write()
    stream.close()
    
    with open() as file_stream:
        operation
'''
```

### 1.1二进制文件

默认都是读取文本文件，并且是 UTF-8 编码的文本文件。要读取二进制文件，比如图片、视频等等，用`'rb'`模式打开文件即可：

```python
f = open('/Users/michael/test.jpg', 'rb')
f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
```

### 1.2字符编码

要读取非UTF-8编码的文本文件，需要给`open()`函数传入`encoding`参数，例如，读取 GBK 编码的文件：

```python
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
f.read()
#'测试'
```

遇到有些编码不规范的文件，你可能会遇到`UnicodeDecodeError`，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，`open()`函数还接收一个`errors`参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

```python
 f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
```

### 1.3写文件

```python
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
```



## 2. StringIO与BytesIO

用于内存中  字符串  与  二进制的读写   用时可以查

## 3.操作文件和目录

如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如`dir`、`cp`等命令。

如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的`os`模块也可以直接调用操作系统提供的接口函数。

```python
import os
print(os.name) #  如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
# 操作系统中定义的环境变量
os.environ
# 要获取某个环境变量的值，可以调用
os.environ.get('key')

'''
os 模块
    os 中常用的方法
    rmdir(dir_name)   删除文件夹  空的
    remove(file_path+file_name) 删除文件
    rmdirs(dir_name)  只能删除  不含文件的文件夹
    getcwd()           获取当前文件所在的文件路径
    listdir(dir_name) 获取文件夹中的所有文件名组成列表
    chdir(dirname) 切换目录
    path 模块
        jion
        dirname
        split
        splitext
        getsize
        exists

        isdir
        isfile
        isabs		# absolute 绝对的
'''
```

## 4.序列化

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了`pickle`模块来实现序列化

```python
import pickle
d = dict(name="Bob",age=20, score=88)
pickle.dumps(d)
'''
b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
'''
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

'''
当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：
'''

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
d
# {'age': 20, 'score': 88, 'name': 'Bob'}
```

Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系

### 4.1 JSON

```python
#Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：

import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)
#'{"age": 20, "score": 88, "name": "Bob"}'
'''
dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
'''
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)	# {'age': 20, 'score': 88, 'name': 'Bob'}

```

