#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/8 15:37


# 笛卡尔积、等值连接、自然连接三者有什么区别
# 区别：
# 　　笛卡尔积对两个关系 R 和 S 进行操作，产生的关系中元组个数为两个关系中元组个 数之积。等值联接则是在笛卡尔积的结果上再进行选择操作，挑选关系第 i 个分量与第(r+j) 个分量值相等的元组；自然连接则是在等值联接(以公共属性值相等为条件)的基础上再行投 影操作，去掉 S 中的公共属性列，当两个关系没有公共属性时，自然连接就转化成笛卡尔 积。
# 1、自然连接一定是等值连接，但等值连接不一定是自然连接。
# 2、等值连接要求相等的分量，不一定是公共属性；而自然连接要求相等的分量必须是公共属性。
# 3、等值连接不把重复的属性除去；而自然连接要把重复的属性除去。
# 笛卡尔积：
# 在数学中，两个集合X和Y的笛卡儿积（Cartesian product），又称直积，表示为X × Y，第一个对象是X的成员而第二个对象是Y的所有可能有序对的其中一个成员。
# 　　假设集合A={a, b}，集合B={0, 1, 2}，则两个集合的笛卡尔积为{(a, 0), (a, 1), (a, 2), (b, 0), (b, 1), (b, 2)}。
# 等值连接：
# 等值连接是关系运算-连接运算的一种常用的连接方式。是条件连接（或称θ连接）在连接运算符为“=”号时（即θ=0时）的一个特例。
# 自然连接：
# 自然连接(Natural join)是一种特殊的等值连接，它要求两个关系中进行比较的分量必须是相同的属性组，并且在结果中把重复的属性列去掉。而等值连接并不去掉重复的属性列。
# -- 第二题：检索年龄大于 17 岁的男学生的学号与姓名
# -- SELECT student.name,student.age,student.gender from student where student.age>17 AND student.gender='男'
#
# -- 第三题 检索学号为 111 学生所学课程的课程名与任课教师名
# -- select course.name,course.teacher from course where course.cno in (SELECT sc.cno from sc where sc.sno = '111')
#
# -- 第四题 检索至少选修 刘老师 所授课程中一门课程的女学生的姓名。
# -- 	链接查询方式(0.030s)
# --  SELECT student.name from student,sc,course where student.sno=sc.sno and sc.cno=course.cno and student.gender='女' and course.teacher='刘老师'
# -- 嵌套查询方式(0.028s)
# -- select student.name from student where student.gender='女' and  student.sno in (select sc.sno from sc where sc.cno in (select course.cno from course where course.teacher='刘老师'))
# --  存在量词的方式(0.031s)
# -- select student.name from student where student.gender='女' and EXISTS(SELECT *from sc where sc.sno=student.sno and EXISTS(SELECT *from course where course.cno=sc.cno and course.teacher='刘老师'))
# -- 第五题 检索 李四 同学不学的课程的课程号
# -- SELECT course.name from course WHERE course.cno not in (SELECT sc.cno from sc WHERE sc.sno in (SELECT student.sno from student WHERE student.name='李四'))
# -- 第六题 查找学习两门以上课程的学生名
# -- SELECT student.name from student where student.sno in (SELECT sc.sno from sc GROUP BY sc.sno HAVING COUNT(sc.cno)>=2)
# -- 第七题
# --   SELECT course.cno,course.name FROM course where NOT EXISTS ( SELECT * FROM student WHERE NOT EXISTS ( SELECT * FROM sc WHERE cno = course.cno AND sno = student.sno ) )
# -- SELECT student.sno,student.name FROM student where NOT EXISTS ( SELECT * FROM course WHERE NOT EXISTS ( SELECT * FROM sc WHERE cno = course.cno AND sno = student.sno ) )
# -- 第八题 检索选修课程包含 黄老师 所授课程的学生学号
# -- SELECT student.sno,student.name from student WHERE student.sno in (SELECT sno from sc where sc.cno in (select cno from course where course.teacher='黄老师'))
#
