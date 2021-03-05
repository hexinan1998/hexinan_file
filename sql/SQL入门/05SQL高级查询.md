# 高级查询

------

## 聚合数据 

### 1.1 聚合函数

假设我们要统计学生表的记录数量，除了直接使用SELECT * FROM Students得到结果集后，通过手动查询数量这种麻烦的方法外，我们可以使用SQL提供的聚合函数 COUNT，快速获得结果。以查询有多少学生为例，我们以下SQL语句：

```sql
SELECT COUNT(*) FROM Students;
/*
结果可能如下
COUNT(*)
6
*/
SELECT COUNT(*) AS StudentsNum FROM Students;
/*
结果可能如下
StudentsNum
6
*/
SELECT COUNT(*) FROM Students WHERE Age > 20;
```

除了count() 外还提供了以下的常用聚合函数：

| 函数 | 说明                                   |
| ---- | -------------------------------------- |
| SUM  | 计算某一列的总和，该列必须为数值类型   |
| AVG  | 计算某一列的平均数，该列必须为数值类型 |
| MAX  | 计算某一列的最大值                     |
| MIN  | 计算某一列的最小值                     |

如果我们要查询学生的平均年龄，就能直接使用AVG聚合函数：

```sql
SELECT AVG(Age) FROM Students;
```

### 1.2 分组

SQL还提供了“分组聚合”功能，帮助我们将具有共性字段的记录整合起来。比如我们想要根据城市City对学生进行分组，并需要查询每个城市有多少学生，可以使用GROUP BY语句：

```sql
SELECT City, COUNT(*) FROM Students GROUP BY City;
```

执行此语句后，GROUP BY子句会按照City将学生进行分组，所有City相同的学生会被放到同一个组中，再进行分别计算，所以COUNT(*)的结果对应的就是特定城市的学生数量。其结果类似以下：

| City          | COUNT(*) |
| ------------- | -------- |
| Beijing       | 1        |
| Los Angeles   | 2        |
| New York City | 1        |
| Shanghai      | 2        |



## 多表查询

SELECT 查询除了能从单表中查数据外，也能从多表中查询数据。语法如下：

```sql
SELECT * FROM table1, table2;
```

## 连接查询

连接查询是另一种类型的多表查询，连接查询会对多个表格进行JOIN运算。也就是说，先确定一个主表作为结果集，然后将其他表的记录有选择性地“嵌入”到主表结果集上。

假设我们想要知道每个学生选择的课程名字，除了上面提到的多表查询加WHERE子句，我们还能使用INNER JOIN子句：

```sql
SELECT S.StudentID, C.CourseName 
FROM Students AS S 
INNER JOIN Courses AS C ON S.CourseID = C.CourseID;
```

此语句就能将每个StudentID和其对应的课程名查询出来，要注意INNSER JOIN语句的内在执行过程如下：

1. 确定主表，使用 FROM table_name
2. 紧接着确认连接的表，使用 INNER JOIN table_name
3. 再确定连接条件，使用 ON condition，上面语句的条件就是 S.CourseID = C.CourseID
4. 最后还能加上 ： WHERE、ORDER BY等子句

除了INNER JOIN外，我们还有LEFT JOIN, RIGHT JOIN, 和FULL JOIN。