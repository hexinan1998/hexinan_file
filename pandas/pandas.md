# pandas

------

```python
import pandas as pd
#pandas有两个主要数据结构：Series 和 DataFrame。
```

## 1.Series

Series是一种类似于一维数组的对象，它由**一组数据**（各种NumPy数据类型）以及一组与之相关的**数据标签（即索引）**组成，即index和values两部分，可以通过索引的方式选取Series中的单个或一组值。

### 1.1创建

**pd.Series(list,intdex = [ ])** 

其中第一个参数可以是列表  ndarray。 也可以是字典，字典的键将作为索。还可以是  DataFrame 中某一行或者某一列

```python
import numpy as np, pandas as pd
arr1  = np.arange(10)
s1 = pd.Series(arr1)
print(s1)
'''
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
9    9
dtype: int32
'''
```

### 1.2常用操作

Series  类型 索引、切片、运算的操作类似于ndarray ，同样的类似Python字典类型的操作，包括保留字in操作、使用.get()方法。
 Series 和 ndarray之间的主要区别在于Series之间的操作会根据索引自动对齐数据

## 2.DataFrame

DataFrame是一个 表格型 的数据类型，每列值类型可以不同，是最常用的pandas对象。DataFrame既有行索引也有列索引，它可以被看做由Series组成的字典（共用同一个索引）。DataFrame中的数据是以一个或多个二维块存放的（而不是列表、字典或别的一维数据结构）。

### 2.1 DaraFrame的创建

**pd.DataFrame(data,columns = [ ],index = [ ])**：

columns和index为指定的列、行索引，并按照顺序排列。

- 创建DataFrame最常用的是直接传入一个由等长列表或NumPy数组组成的**字典**，会自动加上行索引，字典的**键**会被当做**列索引**：

```python
import numpy as np, pandas as pd

dict1 = {
    "name":["zhang san","lis si ","wang wu","ma liu","zhao qi"],
    "age":[18,19,20,17,16],
    "pop":[1.2,3.2,2.1,1.90,2.0]
}
df = pd.DataFrame(dict1)

df2 = pd.DataFrame(dict1,columns=["姓名","年龄","pop","new_data"],index=["one","two","three","four","five"])

print(df)
print(df2)

'''
        name  age  pop
0  zhang san   18  1.2
1    lis si    19  3.2
2    wang wu   20  2.1
3     ma liu   17  1.9
4    zhao qi   16  2.0


       姓名   年龄  pop new_data
one    NaN  NaN  1.2      NaN
two    NaN  NaN  3.2      NaN
three  NaN  NaN  2.1      NaN
four   NaN  NaN  1.9      NaN
five   NaN  NaN  2.0      NaN
'''
```

![DataFrame](D:\download_git\hexinan_study\pandas\img\DataFrame.webp)

### 2.2 DaraFrame对象操作

（1）.**df.values**：将DataFrame转换为ndarray二维数组，注意后面不加()。

（2）通过类似字典标记的方式 或 属性的方式，可以将DataFrame的列获取为一个Series。

（3）列可以通过赋值的方式进行修改。例如，我们可以给那个空的"debt"列赋上一个标量值或一组值。

（4）将列表或数组赋值给某个列时，其长度必须跟DataFrame的长度相匹配。如果赋值的是一个Series，就会精确匹配DataFrame的索引，所有的空位都将被填上缺失值。

（5）为不存在的列赋值会创建出一个新列。关键字del用于删除列。

```python
import pandas as pd
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
df2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five', 'six'])

print(df2.columns)
# output: Index(['year', 'state', 'pop', 'debt'], dtype='object')
#通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series。
print(df2['state'])  #或者df2.state   此时获取一个 Series 对象
'''
Index(['year', 'state', 'pop', 'debt'], dtype='object')
one        Ohio
two        Ohio
three      Ohio
four     Nevada
five     Nevada
six      Nevada
Name: state, dtype: object
'''


#列可以通过赋值的方式进行修改。例如，我们可以给那个空的"debt"列赋上一个标量值或一组值
df2['debt'] = 16.5
print(df2)
'''
       year   state  pop  debt
one    2000    Ohio  1.5  16.5
two    2001    Ohio  1.7  16.5
three  2002    Ohio  3.6  16.5
four   2001  Nevada  2.4  16.5
five   2002  Nevada  2.9  16.5
six    2003  Nevada  3.2  16.5
'''
#将列表或数组赋值给某个列时，其长度必须跟DataFrame的长度相匹配。如果赋值的是一个Series，就会精确匹配DataFrame的索引，所有的空位都将被填上缺失值
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
df2['debt'] = val
print(df2)
'''
        year   state  pop  debt
one    2000    Ohio  1.5   NaN
two    2001    Ohio  1.7  -1.2
three  2002    Ohio  3.6   NaN
four   2001  Nevada  2.4  -1.5
five   2002  Nevada  2.9  -1.7
six    2003  Nevada  3.2   NaN
'''
#为不存在的列赋值，会创建出一个新列
df2['eastern'] = df2.state == 'Ohio'
print(df2)
'''
        year   state  pop  debt  eastern
one    2000    Ohio  1.5   NaN     True
two    2001    Ohio  1.7  -1.2     True
three  2002    Ohio  3.6   NaN     True
four   2001  Nevada  2.4  -1.5    False
five   2002  Nevada  2.9  -1.7    False
six    2003  Nevada  3.2   NaN    False
'''
#关键字del用于删除列
del df2['eastern']
print(df2.columns)
# Index(['year', 'state', 'pop', 'debt'], dtype='object')
```

## 3pandas的基本功能

**数据索引：**Series 和DataFrame的索引是 index 类型的，index对象是不可修改的，可通过索引值或索引标签获取目标数据，也可以通过索引使 序列或数据框的计算、操作实现自动化对齐。索引类型index的常用获取方法：

```python
'''
.append(idx) ：连接另一个Index对象，产生新的Index对象
.diff(idx) ：计算差集，产生新的Index对象
.intersection(idx) ：计算交集
.union(idx) ：计算并集
.delete(loc) ：删除loc位置处的元素
.insert(loc,e)：在loc位置增加一个元素
'''
```

```python
import pandas as pd
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2],
        'price':[3000,4000,2600,3400,4100,8000]
        }
df = pd.DataFrame(data,index=["one","two","three","four","five","six"])

nc = df.columns.delete(2)
ni = df.index.insert(6,"one")

nd = df.reindex(columns=nc,index = ni).ffill()
print(nd)
'''
        state  year  price
one      Ohio  2000   3000
two      Ohio  2001   4000
three    Ohio  2002   2600
four   Nevada  2001   3400
five   Nevada  2002   4100
six    Nevada  2003   8000
one      Ohio  2000   3000
'''
```



**重新索引**：能够改变、重排Series和DataFrame索引，会创建一个新对象，如果某个索引值当前不存在，就引入缺失值。
 **df.reindex(index, columns ,fill_value, method, limit, copy )**：index/columns为新的行列自定义索引；fill_value为用于填充缺失位置的值；method为填充方法，ffill当前值向前填充，bfill向后填充；limit为最大填充量；copy 默认True，生成新的对象，False时，新旧相等不复制。

```python
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(9).reshape(3,3),
                     index=["a","b","c"],
                     columns=["d","e","f"])
print(frame)
frame2 = frame.reindex(index = ["a","b","g","c",],columns=["d","e","f","h"])
print(frame2)
'''
   d  e  f
a  0  1  2
b  3  4  5
c  6  7  8
     d    e    f   h
a  0.0  1.0  2.0 NaN
b  3.0  4.0  5.0 NaN
g  NaN  NaN  NaN NaN
c  6.0  7.0  8.0 NaN
'''
```

**删除指定索引**：默认返回的是一个新对象。
 **.drop()**：能够删除Series和DataFrame指定行或列索引。
 删除一行或者一列时，用单引号指定索引，删除多行时用列表指定索引。
 如果删除的是列索引，需要增加axis=1或axis='columns'作为参数。
 增加inplace=True作为参数，可以就地修改对象，不会返回新的对象。

```python
import pandas as pd
a = pd.Series([1,2,3,4],index=["a","b","c","d"])
print(a)
print(a.drop(["a"]))
'''
a    1
b    2
c    3
d    4
dtype: int64
b    2
c    3
'''
```

```python
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.arange(9).reshape(3,3),
                     index=["a","b","c"],
                     columns=["d","e","f"])
frame2 = frame.reindex(index = ["a","b","g","c",],columns=["d","e","f","h"])
print(frame2.drop("a"))
print(frame2.drop("d",axis="columns"))
'''
     d    e    f   h
b  3.0  4.0  5.0 NaN
g  NaN  NaN  NaN NaN
c  6.0  7.0  8.0 NaN
     e    f   h
a  1.0  2.0 NaN
b  4.0  5.0 NaN
g  NaN  NaN NaN
c  7.0  8.0 NaN
'''
```

**索引、选取和过滤**
 **df.loc[行标签，列标签]**：通过标签查询指定的数据，第一个值为行标签，第二值为列标签。当第二个参数为空时，查询的是单个或多个行的所有列。如果查询多个行、列的话，则两个参数用列表表示。
 **df.iloc[行位置，列位置]**：通过默认生成的数字索引查询指定的数据

```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(9).reshape(3,3),
                     index=["a","b","c"],
                     columns=["d","e","f"])
print(df.loc["a",["d","e"]])
print(df.iloc[0,[1,2]])
'''
d    0
e    1
Name: a, dtype: int32
e    1
f    2
Name: a, dtype: int32
'''
```

![pands重新选取与组合数据](D:\download_git\hexinan_study\pandas\img\pands重新选取与组合数据.webp) 

**算术运算**：算术运算根据行列索引，对齐后运算，运算默认产生浮点数，对齐时缺项填充NaN (空值)。除了用+-*/外，还可以用Series和DataFrame的算术方法，这些方法传入fill_value参数时，可以填充缺省值。比如

df1.add(df2, fill_value = 1)：

![img](D:\download_git\hexinan_study\pandas\img\03.webp)

比较运算只能比较相同索引的元素，不进行补齐。采用>< >= <= == !=等符号进行的比较运算，产生布尔值。

**排序** ：在排序时，任何缺失值默认都会被放到末尾
 **.sort_index(axis=0, ascending=True)**：根据指定轴索引的值进行排序。默认轴axis=0, ascending=True，即默认根据0轴的索引值做升序排序。轴axis=1为根据1轴的索引值排序， ascending=False为降序。
 在指定轴上根据数值进行排序，默认升序。
 **Series.sort_values(axis=0, ascending=True)**：只能根据0轴的值排序。
 **DataFrame.sort_values(by, axis=0, ascending=True)**，参数by为axis轴上的某个索引或索引列表。

##  4 pandas数据分析

**.describe()**：针对各列的多个统计汇总，用统计学指标快速描述数据的概要。
 **.sum()**：计算各列数据的和
 **.count()**：非NaN值的数量
 **.mean( )/.median()**：计算数据的算术平均值、算术中位数
 **.var()/.std()**：计算数据的方差、标准差
 **.corr()/.cov()**：计算相关系数矩阵、协方差矩阵，是通过参数对计算出来的。Series的corr方法用于计算两个Series中重叠的、非NA的、按索引对齐的值的相关系数。DataFrame的corr和cov方法将以DataFrame的形式分别返回完整的相关系数或协方差矩阵。
 **.corrwith()**：利用DataFrame的corrwith方法，可以计算其列或行跟另一个Series或DataFrame之间的相关系数。传入一个Series将会返回一个相关系数值Series（针对各列进行计算），传入一个DataFrame则会计算按列名配对的相关系数。
 **.min()/.max()**：计算数据的最小值、最大值
 **.diff()**：计算一阶差分，对时间序列很有效
 **.mode()**：计算众数，返回频数最高的那（几）个
 **.mean()**：计算均值
 **.quantile()**：计算分位数（0到1）
 **.isin()**：用于判断矢量化集合的成员资格，可用于过滤Series中或DataFrame列中数据的子集
 **适用于Series的基本统计分析函数，DataFrame[列名]返回的是一个Series类型。**
 **.unique()**：返回一个Series中的唯一值组成的数组。
 **.value_counts()**：计算一个Series中各值出现的频率。
 **.argmin()/.argmax()**：计算数据最大值、最小值所在位置的索引位置（自动索引）
 **.idxmin()/.idxmax()**：计算数据最大值、最小值所在位置的索引（自定义索引

## 5 pandas读写文本格式的数据

pandas提供了一些用于将表格型数据读取为DataFrame对象的函数。下表对它们进行了总结，其中read_csv()、read_table()、to_csv()是用得最多的。

 ![pandas读写文件](D:\download_git\hexinan_study\pandas\img\pandas读写文件.webp) 

## 6 用pandas来进行数据清洗和准备

```python
#    处理缺失数据   删除重复数据   数据替换 （替换值）（利用函数或者字典 进行数据转换）
```

## 7 DataFrame常见函数

df.head()：查询数据的前五行
 df.tail()：查询数据的末尾5行
 pandas.cut()
 pandas.qcut() 基于分位数的离散化函数。基于秩或基于样本分位数将变量离散化为等大小桶。
 pandas.date_range() 返回一个时间索引
 df.apply() 沿相应轴应用函数
 Series.value_counts() 返回不同数据的计数值
 df.aggregate()
 df.reset_index() 重新设置index，参数drop = True时会丢弃原来的索引，设置新的从0开始的索引。常与groupby()一起用
 numpy.zeros()