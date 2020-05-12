#!/usr/bin/env python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : guanyu
# @Time    : 2020/3/27 9:57 上午
# @File    : gui.py
# software: PyCharm


import tkinter.filedialog as filedialog
from tkinter import *
import os
from tkinter import *
import tkinter as tk
#import vlookup
import pandas as pd


def change(widget, var):
    """事件处理函数：改变Text部件的文本
    在widget现有文本末尾插入新的文本var
    """
    widget.config(state="normal")
    widget.insert("end", var + "\n")
    # 限制text窗口 不可编辑。只可以输入。
    widget.config(state="disabled")

# 获取文件路径
def callback(entry11):
    entry11.delete(0, END)  # 清空entry里面的内容，在顶部
    # text.delete(0, END)
    # 调用filedialog模块的askdirectory()函数去打开文件夹
    global filepath
    filepath = filedialog.askopenfilename()
    if filepath:
        entry11.insert(0, filepath)  # 将选择好的路径加入到entry里面

# 获取保存文件路径
def callback1(entry1):
    entry1.delete(0, END)  # 清空entry里面的内容，在顶部
    # text.delete(0, END)
    # 调用filedialog模块的askdirectory()函数去打开文件夹
    global folderpath
    folderpath = filedialog.askdirectory()  # 获得选择好的文件夹
    if folderpath:
        entry1.insert(0, folderpath)  # 将选择好的路径加入到entry里面


def main():
    root = tk.Tk()
    root.title("值域对照 V1.0")
    root.geometry("600x500")
    root.rowconfigure(1, weight=1)
    root.rowconfigure(4, weight=8)

    #def about():
    w=Label(root,text="使用方法：选择要对照的文件（院标文件、国标文件）点击添加按钮，\n选择对照完成文件保存位置，点击添加按钮，\n最后点击运行"
                      "\n说明：目前该版本为初版，有时间后续会更新。",background="wheat")
    w.grid(sticky=W + N, row=5, column=0,columnspan=4)#, padx=5, pady=5)
    w.place(x=50, y=400)

    # 创建entry 框
    entry = Entry(root, width=55)
    entry.grid(sticky=W + N, row=0, column=0, columnspan=4, padx=5, pady=5)

    # 创建button按钮 选择文件  调用callback 选择文件，并传给entry
    button = Button(root, text=" 选择文件",width=8, height=2, command=lambda: callback(entry))
    button.grid(sticky=W + N, row=1, column=0)#, padx=5, pady=5)
    button.place(x=20, y=40)
    #print(entry)

    # 创建text窗口，存放选择的文件路径
    text = tk.Text(root, width=65, height=20, background="wheat")
    text.config(state="disabled")
    text.place(x=24, y=100)

    # 添加按钮，选择文件到entry 调用change函数把 entry中内容 传给text  把选择的文件和文件夹都传给text
    button3 = tk.Button(root, text="添   加",width=6, height=2,command=lambda: change(text, entry.get()))
    button3.grid(sticky=W + N, row=1, column=1)#, padx=5, pady=5)
    button3.place(x=140, y=40)

    # 文件要保存的路径
    button4 = tk.Button(root, text="生成文件保存路径",width=15, height=2, command=lambda:callback1(entry))
    button4.grid(sticky=W + N, row=1, column=2)#, padx=5, pady=5)
    button4.place(x=240, y=40)

    # 提交处理
    button2 = tk.Button(root, text="运   行",width=6, height=2, command=lambda: merge())#data1=text.get(1.0), data2= text.get(2.0), all_data=text.get(3.0)))
    button2.grid(sticky=W + N, row=1, column=3, padx=5, pady=5)
    button2.place(x=430, y=40)

    # # 清空text
    # button5 = tk

    def merge():
        # 院标文件未知 需修改为对应的位置
        filepath_all = text.get(1.0,END).split("\n")
        print(filepath_all)
        data1 = pd.read_excel(filepath_all[0], encoding='gbk')

        # 国标文件位置 需修改为对应的位置
        data2 = pd.read_excel(filepath_all[1], encoding='gbk')
        # mergr中 on 后参数，对应原表中两列的名称，并且 两列的名称需要相同。 例如：
        # 合并两列, 默认方法是how=inner, 只合并相同的部分, how的取值可以为['left', 'right', 'outer', 'inner']
        # on用于连接的列索引 必须保证左右都有该列名
        all_data = pd.merge(data1, data2, on=['名称'], how='outer')
        # 输出的位置
        all_data.to_excel(filepath_all[2] +'/'+ '对照.xlsx',"w")
        # print(all_data)
        print("对照完成")
        change(text, "对照完成，点退出按钮，退出程序" + "\n")

    # 退出程序窗口
    b = Button(root, text='退   出',width=6, height=2, command=root.quit)
    b.grid(sticky=W + N, row=4, column=3)#, padx=5, pady=5)
    b.place(x=500, y=420)

    # 窗口循环
    root.mainloop()
    #print(text)
    #print(entry.get())



# 主函数
if __name__ == "__main__":
    main()
