#导入模块
import pymysql.cursors
import requests

def duizhao():
    #建立连接通道，建立连接填入（连接数据库的IP地址，端口号，用户名，密码，要操作的数据库，字符编码）
    connection = pymysql.connect(host = "localhost",user='root', passwd='guanyu666', database='jxc',port=3306,charset='utf8')
    cursor = connection.cursor()
    #查询SQL
    ex=cursor.execute("select * from 国标 a left join 院标 b on a.国标值含义 = b.手术名称 union select * from 国标 a right join 院标 b on a.国标值含义 = b.手术名称")

    books = cursor.fetchmany(ex)
    for book in books:
        print(book)

    connection.close()

    #data = cur.fetchall() #所有
    #for item in data:
    #    print(item)
    #db.close()



#!/usr/bin/env python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

# data1 = pd.read_excel('/Users/guanyu/医疗相关/05互联互通项目/006垂杨柳医院/值域对照/Nsv_Ssv_20181220133042_2.xlsx', encoding='gbk',rigth_on='国标值含义' )
# data2 = pd.read_excel('/Users/guanyu/医疗相关/05互联互通项目/006垂杨柳医院/值域对照/手术代码.xls', encoding='gbk',left_on='手术名称' )
# # # 合并两列, 默认方法是how=inner, 只合并相同的部分, how的取值可以为['left', 'right', 'outer', 'inner']
# all_data = pd.merge(data1,data2,on = ['手术名称','手术名称'],how='outer' )
# all_data.to_excel('/Users/guanyu/医疗相关/05互联互通项目/006垂杨柳医院/值域对照/new_data.xlsx')
# print(all_data)


##,how='outer'


##值域对照

import pandas as pd
# 院标文件未知 需修改为对应的位置
data1 = pd.read_excel('/Users/guanyu/Desktop/中医诊断.xlsx', encoding='gbk',rigth_on='院标名称' )   #
# 国标文件位置 需修改为对应的位置
data2 = pd.read_excel('/Users/guanyu/Desktop/中医病证与分类.xlsx', encoding='gbk',left_on='国标名称' ) #名称列复制一列再后

'''### mergr中 on 后参数，对应原表中两列的名称，并且 两列的名称需要相同。 例如：
院标代码	名称
111424	肝经湿热证
111425	肝经郁火证
111426	肝经郁热证

国标代码	名称	    国标名称1
BN	    内科病	内科病
BNF	    肺系病类	肺系病类
BNF010	咳嗽病	咳嗽病

'''
# 合并两列, 默认方法是how=inner, 只合并相同的部分, how的取值可以为['left', 'right', 'outer', 'inner']  on用于连接的列索引 必须保证左右都有该列名
all_data = pd.merge(data1,data2,on = ['名称'],how='outer' )
# 输出的位置
all_data.to_excel('/Users/guanyu/Desktop/中医病证与分类对照.xlsx')
print(all_data)

