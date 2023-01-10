import pymysql

#连接数据库
db = pymysql.connect(host='localhost',user='root',password='root',db='userinfocheck')

#使用cursor()方法创建一个游标对象
cursor = db.cursor()

#使用execute()方法执行SQL语句
cursor.execute('SELECT COUNT(*) FROM longu WHERE score')

#使用fetall()获取全部数据
data1 = cursor.fetchall()

cursor.execute('select sum(score) from longu')
data2 = cursor.fetchall()

#打印获取到的数据
print("长评分数之和："+str(data2[0][0]))
print("长评分数人数："+str(data1[0][0]))
print("评分为："+str(data2[0][0]/data1[0][0]))
print()

#使用execute()方法执行SQL语句
cursor.execute('SELECT COUNT(*) FROM shortu WHERE score')

#使用fetall()获取全部数据
data1 = cursor.fetchall()

cursor.execute('select sum(score) from shortu')
data2 = cursor.fetchall()

#打印获取到的数据
print("短评分数之和："+str(data2[0][0]))
print("短评分数人数："+str(data1[0][0]))
print("评分为："+str(data2[0][0]/data1[0][0]))
#关闭游标和数据库的连接


print()
cursor.execute('select COUNT(*) from longu where vipName="年度大会员"')
data1 = cursor.fetchall()
print("参与 长评 打分比例构成：年度大会员："+str(data1[0][0])+"     ",end="")
cursor.execute('select sum(score) from longu where vipName="年度大会员"')
data2 = cursor.fetchall()
print("平均打分："+str(data2[0][0]/data1[0][0])+"     ")


cursor.execute('select COUNT(*) from longu where vipName="大会员"')
data1 = cursor.fetchall()
print("参与 长评 打分比例构成：大会员："+str(data1[0][0])+"     ",end="")
cursor.execute('select sum(score) from longu where vipName="大会员"')
data2 = cursor.fetchall()
print("平均打分："+str(data2[0][0]/data1[0][0])+"     ")


cursor.execute('select COUNT(*) from longu where vipName=""')
data1 = cursor.fetchall()
print("参与 长评 打分比例构成：普通用户："+str(data1[0][0])+"     ",end="")
cursor.execute('select sum(score) from longu where vipName=""')
data2 = cursor.fetchall()
print("平均打分："+str(data2[0][0]/data1[0][0])+"     ")


print()
cursor.execute('select COUNT(*) from shortu where vipName="年度大会员"')
data1 = cursor.fetchall()
print("参与 短评 打分比例构成：年度大会员："+str(data1[0][0])+"     ",end="")
cursor.execute('select sum(score) from shortu where vipName="年度大会员"')
data2 = cursor.fetchall()
print("平均打分："+str(data2[0][0]/data1[0][0])+"     ")


cursor.execute('select COUNT(*) from shortu where vipName="大会员"')
data1 = cursor.fetchall()
print("参与 短评 打分比例构成：大会员："+str(data1[0][0])+"     ",end="")
cursor.execute('select sum(score) from shortu where vipName="大会员"')
data2 = cursor.fetchall()
print("平均打分："+str(data2[0][0]/data1[0][0])+"     ")


cursor.execute('select COUNT(*) from shortu where vipName=""')
data1 = cursor.fetchall()
print("参与 短评 打分比例构成：普通用户："+str(data1[0][0])+"     ",end="")
cursor.execute('select sum(score) from shortu where vipName=""')
data2 = cursor.fetchall()
print("平均打分："+str(data2[0][0]/data1[0][0])+"     ")

print()
cursor.execute('select content,likes from longu ORDER BY likes DESC limit 5')
data1 = cursor.fetchall()
for i in range(5):
    print("长评点赞第{}的评论：{}".format(i+1,data1[i][0]))
    print("点赞数：{}".format(data1[i][1]))

print()
cursor.execute('select content,replys from longu ORDER BY replys DESC limit 5')
data1 = cursor.fetchall()
for i in range(5):
    print("长评差评第{}的评论：{}".format(i+1,data1[i][0]))
    print("差评数：{}".format(data1[i][1]))

print()
cursor.execute('select COUNT(*) from longu where score=10')
data2 = cursor.fetchall()
print("长评打10分人数："+str(data2[0][0])+"     ")
cursor.execute('select COUNT(*) from longu where score=8')
data2 = cursor.fetchall()
print("长评打8分人数："+str(data2[0][0])+"     ")
cursor.execute('select COUNT(*) from longu where score=6')
data2 = cursor.fetchall()
print("长评打6分人数："+str(data2[0][0])+"     ")
cursor.execute('select COUNT(*) from longu where score=4')
data2 = cursor.fetchall()
print("长评打4分人数："+str(data2[0][0])+"     ")
cursor.execute('select COUNT(*) from longu where score=2')
data2 = cursor.fetchall()
print("长评打2分人数："+str(data2[0][0])+"     ")

print()
cursor.execute('select COUNT(*) from shortu where score=10')
data2 = cursor.fetchall()
print("短评论打10分人数："+str(data2[0][0])+"     ")
cursor.execute('select COUNT(*) from shortu where score=8')
data2 = cursor.fetchall()
print("短评打8分人数："+str(data2[0][0])+"     ")
cursor.execute('select COUNT(*) from shortu where score=6')
data2 = cursor.fetchall()
print("短评打6分人数："+str(data2[0][0])+"     ")
cursor.execute('select COUNT(*) from shortu where score=4')
data2 = cursor.fetchall()
print("短评打4分人数："+str(data2[0][0])+"     ")
cursor.execute('select COUNT(*) from shortu where score=2')
data2 = cursor.fetchall()
print("短评打2分人数："+str(data2[0][0])+"     ")


cursor.close()
db.close()