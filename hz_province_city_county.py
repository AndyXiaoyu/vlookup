#!/usr/bin/env python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : guanyu
# @Time    : 2020/5/13 5:37 下午
# @File    : hz_province_city_county.py
# software: PyCharm

import os
# 解决oracle数据库乱码问题 ps:oracle简直了。。。
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# 导入oracle 包
import cx_Oracle
#import pymysql
import cpca
import datetime
# import mysql.connector

# 第一种方法，查询数据库中长地址列，进行拆分，把拆分后四列插入数据库相应列中。
# 导入访问MySQL的模块

## 1、连接数据库  替换连接信息
#db1 = pymysql.connect('127.0.0.1', 'root', 'guan', 'ivy_db')
# 源数据库连接
db1 = cx_Oracle.connect('hz_hlht/oracle@155.155.55.6:1521/hzcdrpdb')
# 获取游标
curfrom = db1.cursor()
# 目标数据库连接
db2 = cx_Oracle.connect('hz_hlht/oracle@155.155.55.6:1521/hzcdrpdb')

# 获取游标
curto = db2.cursor()

# 以下代码用于首次 导入------------->
## 3、调用执行select语句查询数据
##row = cursor1.execute("SELECT JTZZ,BRXM,WYH,BRXH,LRRQ,CYRQ FROM ba.ba_brjbxx where BRXM> '%s' and "
                     # " WYH IS NOT NULL and CYRQ >TO_DATE('2018-01-01 00:00:00','yyyy-mm-dd hh24:mi:ss')")

row = curfrom.execute("SELECT INHOSP_INDEX_NO,DISCHARGE_DATE,CURR_ADDR_PROVINCE,BIRTH_ADDR_PROVINCE,ADDR_COMPANY_PROVINCE,HUKOU_ADDR_PROVINCE,CONTACT_PERSON_ADDR_PROVINCE FROM PAT_INPUT_CASE_FIRP where INHOSP_INDEX_NO > '%s' and DISCHARGE_DATE >=('20180101000000')")
#print(row)
for row in curfrom:
    #print(row[0] + '-->' + row[1])
    df = cpca.transform(row, cut=False)
    #print(row)
## 4、拆分后数据写入数据库
    ## 插入新数据
    # sql = """INSERT INTO ewell.zy_hzdz(province,city,area,street,BRXM,WYH,BRXH,LRRQ,CYRQ) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""\
    #      %(df.iloc[0, 0],df.iloc[0, 1],df.iloc[0, 2],df.iloc[0, 3][4:],row[1],row[2],row[3],row[4],row[5])
    #cursor2.execute(sql)
    print(row[1],row[2],df.iloc[0, 0],df.iloc[0, 1],df.iloc[0, 2],df.iloc[0, 3],df.iloc[0, 4],df.iloc[1, 5],df.iloc[1, 6],df.iloc[1, 7])
    ## 提交到数据库
    # db2.commit()
# ##<----------------首次导入语句结束

# 以下代码用于增量导入------------->

# 按天增量抽取，查询昨天的数据
# yesStr1 = ((datetime.datetime.now()- datetime.timedelta(days=1)))#.date())
# sqls = "select JTZZ,BRXM,WYH,BRXH,LRRQ,CYRQ from ba.ba_brjbxx where LRRQ > TO_DATE(substr('%s',1,10),'yyyy-mm-dd hh24:mi:ss')" % yesStr1
# # sqls = curfrom.execute("SELECT JTZZ,BRXM,WYH,BRXH FROM ba.ba_brjbxx where BRXM> '%s' and "
#                      # " WYH IS NOT NULL and LRRQ = TO_CHAR('%s','yyyy-mm-dd hh24:mi:ss') ") %yesStr1
# #print(yesStr1)
# curfrom.execute(sqls)
# # 接收查询出的数据
# rows = curfrom.fetchall()
# #print(rows)
# for row in rows:
#     df = cpca.transform(row, cut=False,open_warning=False)
#     # print (row)
#     sqlstr = """insert into ewell.zy_hzdz(province,city,area,street,BRXM,WYH,BRXH,LRRQ,CYRQ) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""\
#           %(df.iloc[0, 0],df.iloc[0, 1],df.iloc[0, 2],df.iloc[0, 3][4:],row[1],row[2],row[3],row[4],row[5])
#     #print(sqlstr)
#     curto.execute(sqlstr)
#     print(df.iloc[0, 0],df.iloc[0, 1],df.iloc[0, 2],df.iloc[0, 3][4:],row[1],row[2],row[3],row[4],row[5])
#     # 提交到数据库
#     db2.commit()
# <----------------增量导入语句结束


## 5、关闭游标
curfrom.close()
curto.close()

## 6、关闭连接
db1.close()
db2.close()

