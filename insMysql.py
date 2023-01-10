import xlrd
import pymysql

# 打开数据所在的路径表名
book = xlrd.open_workbook('S:\\PythonStudy\\b站评分查询\\三体评分人数长评.xlsx')
# 这个是表里的sheet名称（注意大小写）
sheet = book.sheet_by_name('sheet1')

# 建立一个 MySQL连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='root',
    db='userinfocheck',
    port=3306,
    charset='utf8'
)

# 获得游标
cur = conn.cursor()

# 创建插入sql语句
query = 'insert into longu(mid,vipName,content,progress,ctime,likes,replys,score)values(%s,%s,%s,%s,%s,%s,%s,%s)'

# 创建一个for循环迭代读取xls文件每行数据的，
# 从第二行开始是要跳过标题行
# 括号里面1表示从第二行开始(计算机是从0开始数)
for r in range(1, sheet.nrows):
    # (r, 0)表示第二行的0就是表里的A1:A1
    mid = sheet.cell(r, 0).value
    vipName = sheet.cell(r, 1).value
    content = sheet.cell(r, 2).value
    progress = sheet.cell(r, 3).value
    ctime = sheet.cell(r, 4).value
    likes = sheet.cell(r, 5).value
    replys = sheet.cell(r, 6).value
    score = sheet.cell(r, 7).value


    values = (mid,vipName,content,progress,ctime,likes,replys,score)
    # 执行sql语句
    cur.execute(query, values)

# close关闭文档
cur.close()
# commit 提交
conn.commit()
# 关闭MySQL链接
conn.close()
# 显示导入多少列
columns = str(sheet.ncols)
# 显示导入多少行
rows = str(sheet.nrows)
print('导入'+columns+'列'+rows+'行数据到MySQL数据库!')