# SQL查询

------

## 数据查询

查询基本语法

```sql
SELECT * FROM TABLE_NAME;

SELECT * FROM Students;
```

条件查询

```sql
SELECT * FROM TABLE_NAME WHERE condition;

SELECT * FROM Students WHERE Age>1;
//条件表达式
...  WHERE condition1 AND condition2;

SELECT * FROM Students WHERE Age>20 AND Gender="M";

...  WHERE condition1 OR condition2;

SELECT * FROM Students WHERE Age>20 OR Gender="M";

...  WHERE NOt condition;

SELECT * FROM Students WHERE NOT Gander="F";
<=====>  
SELECT * FROM Students WHERE Gander<>"F"


 // 多条件   可以使用 () 条件表达式
 
 SELECT * FROM Students
 WHERE (Age > 22 or Age < 20) AND Gender='M';
```

投影查询



排序查询

```sql
//单列排序 
SELECT * FROM Students ORDER BY Agc ASC / DESC;
//多条件排序
SELECT * FROM Students ORDER BY Agc ASC,Gender;
//缩小范围排序
SELECT * FROM Srudents
WHERE City = "Shanghai"
ORDER BY Age;
```

## 练习

```sql
// 选取年纪大于 20 ，并且来自上海 ，将结果按照 ，从小到大排好序。最后结果只需要 StudentID 字段。

SELECT StudentID FROM Students
WHERE age > 20 AND Cicty = 'shanghai'
ORDER BY Age; 

```

