##,how='outer'


##值域对照
import pandas as pd
def main():
    # 院标文件未知 需修改为对应的位置
    data1 = pd.read_excel('/Users/guanyu/Desktop/中医诊断.xlsx', encoding='gbk',rigth_on='院标名称' )   #
    # 国标文件位置 需修改为对应的位置
    data2 = pd.read_excel('/Users/guanyu/Desktop/中医病证与分类.xlsx', encoding='gbk',left_on='国标名称' ) #名称列复制一列再后

    # 合并两列, 默认方法是how=inner, 只合并相同的部分, how的取值可以为['left', 'right', 'outer', 'inner']  on用于连接的列索引 必须保证左右都有该列名
    all_data = pd.merge(data1,data2,on = ['名称'],how='outer' )
    # 输出的位置
    all_data.to_excel('/Users/guanyu/Desktop/中医病证与分类对照.xlsx')
    print(all_data)

if __name__ == "__main__":
    main()

