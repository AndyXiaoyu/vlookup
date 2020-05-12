import pymysql
import xlwt
import os
# import pandas as pd


# 在数据库中，匹配值域，获取数据库列 匹配两列数据 并导出
# database conn
def dbConnect(dburl):
    db_conn = pymysql.connect(host = "localhost",user='root', passwd='guanyu666', database='jxc',port=3306,charset='utf8')
    return db_conn

#获取列名
def getCol(opt):
    db_conn = dbConnect("localhost")
    cursor  = db_conn.cursor()
    cursor.execute(opt)
    col = tuple([tuple[0] for tuple in cursor.description])
    db_conn.close()
    return col

#获取数据
def sqlOpt(opt):
    db_conn = dbConnect("localhost")
    cursor  = db_conn.cursor()
    cursor.execute(opt)
    data = cursor.fetchall()
    # final_data = col + data
    db_conn.close()
    return data

# 写入文件
def write_into_excel(col_name, content):
    os.chdir("/Users/guanyu/医疗相关")
    #filename=input("请输入要保存的文件名,无需后缀:") + '.xls'
    filename = '导出.xls'
    wbk=xlwt.Workbook(encoding='utf-8')
    test=wbk.add_sheet('test', cell_overwrite_ok=True)

    fileds=list(col_name)
    trans_data = list(content)
    # 写入列名
    for filed in range(0, len(fileds)):
        test.write(0, filed, fileds[filed])
    for row in range(1, len(trans_data)+1):
        for col in range(0, len(fileds)):
            test.write(row, col, u'%s' % str(trans_data[row-1][col]))
    wbk.save(filename)
    print("数据导出成功！")

# 主函数
def run_Task():
    sql = "select * from 国标 a left join 院标 b on a.国标值含义 = b.手术名称 union select * from 国标 a right join 院标 b on a.国标值含义 = b.手术名称"
    result = sqlOpt(sql)
    col_name = getCol(sql)
    # print(result)
    # print(col_name)
    write_into_excel(col_name, result)

run_Task()
