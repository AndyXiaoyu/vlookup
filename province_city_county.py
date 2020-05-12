#!/usr/bin/env python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : guanyu
# @Time    : 2019-08-22 16:18
# @File    : province_city_county.py
# software: PyCharm

## 拆分数据库中长地址
## 导入以下模块
import pymysql
import xlwt
import os
import pandas as pd
import cpca

## 第一种方法，查询数据库中长地址列，进行拆分，把拆分后四列插入数据库相应列中。
## 导入访问MySQL的模块
import mysql.connector

## 1、连接数据库  替换连接信息
db1 = pymysql.connect('127.0.0.1', 'root', 'guanyu666', 'ivy_db')

## 2、获取游标
cursor1 = db1.cursor()

## 3、调用执行select语句查询数据
row = cursor1.execute("SELECT ID_ADDRESS FROM pb_vip_id where ID_ADDRESS > '%s';", (0,))

for row in cursor1:
    #print(row)
    #print(row[0] + '-->' + row[1])
    df = cpca.transform(row, cut=False)
    #df
    #print(df)

## 4、拆分后数据写入数据库
    ## 目标库连接信息，可以是同一个库      DataFrame.values
    db2 = pymysql.connect('127.0.0.1', 'root', 'guanyu666', 'ivy_db')
    cursor2 = db2.cursor()
    ## 插入语句  接收传递参数：%s  需写成'%s'
    ## 更新现有数据
    #sql = """UPDATE pb_vip_id_out SET province = '%s',city='%s',area='%s',street='%s';"""  %(df.iloc[0, 0], df.iloc[0, 1], df.iloc[0, 2],df.iloc[0, 3])
    print(df.iloc[0, 0], df.iloc[0, 1], df.iloc[0, 2],df.iloc[0, 3])
    ## 插入新数据
    sql = """INSERT INTO pb_vip_id_out(province,city,area,street) value('%s','%s','%s','%s')"""%(df.iloc[0, 0], df.iloc[0, 1], df.iloc[0, 2],df.iloc[0, 3])
    cursor2.execute(sql)
    ## 提交到数据库
    db2.commit()

## 5、关闭游标
cursor1.close()
cursor2.close()

## 6、关闭连接
db1.close()
db2.close()


# 第二种方法，通过文件读取拆分
#读取数据
# import pandas as pd
# origin = pd.read_excel( "/Users/guanyu/PycharmProjects/vlookup/ID_ADDRESS.xlsx" )
#
#  #转换
# import cpca
# addr_df = cpca.transform(origin[ "ID_ADDRESS"], cut=False, lookahead=5)
#
#  #输出
# print(addr_df)
#
# processed = pd.concat([origin, addr_df],axis = 1 )
# processed.to_excel( "processed.xlsx" , index = False , encoding = "utf-8" )





# #省市区拆分
# location_str = ["内蒙古巴彦淖尔市临河区曙光西街5栋2单元301号"]
# import cpca
# df = cpca.transform(location_str, cut=False, lookahead=3)
# df
# print(df)
# #全地址
# #         省      市    区                     地址
# # 0  内蒙古自治区  巴彦淖尔市  临河区  巴彦淖尔市临河区曙光西街5栋2单元301号
#
#
#
# location_str = ["内蒙古巴彦淖尔市临河区曙光西街5栋2单元301号"]
# import cpca
# df = cpca.transform(location_str, cut=False)
# df
# print(df)
# # 拆分地址
# #         省      市    区             地址
# # 0  内蒙古自治区  巴彦淖尔市  临河区  曙光西街5栋2单元301号
