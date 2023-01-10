import pymysql

#打开数据库连接
db = pymysql.connect(host='3306',user='root',password='root',db='longu')

#创建游标对象
cursor = db.cursor()

#使用execute()方法执行sql语句
cursor.execute('select version()')

#fetchone()方法获取返回对象的单条数据
data = cursor.fetchone()
print('Database version:{0}'.format(data))

#关闭数据库连接
db.close()