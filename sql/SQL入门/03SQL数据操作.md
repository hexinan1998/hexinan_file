​	

```sql
DROP TABLE student;
// 创建
CREATE TABLE student(
    StudentID int,
    Name varchar(255),
    City varchar(255),
    PRIMARY KEY(StudentID)
);
// 修改数据库  ALTER（修改）
ALTER TABLE table_name
ADD age int;

ALTER TABLE table_name
DROP COLUMN Age;

ALTER TABLE table_name
MODIFY COLUMN Name varchar(200);
```

```sql
//记录操作
 CRDN ( create、delete、update、retrieve)

INSERT : 插入新 记录 
UPDATE : 更新已有 记录
DELETE : 删除已有记录

//插入新记录
INSERT INTO table_name(column1,column2,column3,...)
VALUES(value1,value2,value3,...)
//例子
INSERT INTO student(StudentID,Name,City)
VALUES(1,"HEXINAN","sanmenxia")

// 使用 values() 直接修改 如果字段不够的话，会报错
INSERT INTO table_name VALUES(value1,value2,value3)
//例子
INSERT INTO table_name VALUES(1,"HEXINAN","sanmenxia")


// 更新记录 
UPDATE table_name
SET column1 = value1 ,colummn2 = value2,...
WHERE condition;
//例子
UPDATE Srudents;
SET Name = "hexinan"
where studentid > 1;

// 删除记录
DELETE FROM TABLE WHERE condition;
//例子
DELETE FROM TABLE WHERE City = 'sanmenxia';

// 替换记录

```

```sql
//约束  constraint

CREATE TABLE Employees(
  EmployeeID int Primary Key,
  Name varchar(255) NOT NULL,
  Apartment varchar(255) DEFAULT 'A',
  Age int CHECK (Age > 18)
);

ALTER TABLE Students
MODIFY Age int NOT NULL;


ALTER TABLE Students
ADD CONSTRAINT fk_class_id
FOREIGN key (classID)
REFERENS Classes(id);

```

