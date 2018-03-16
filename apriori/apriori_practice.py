# 关联算法
from apriori import find_rule
import pandas as pda
filename='lesson_buy.xls'
# 转化为pandas的数组框形式，
dataframe=pda.read_excel(filename,header=None)

# 转化一下数据,index 表示Series的下标
change=lambda x:pda.Series(1,index=x[pda.notnull(x)])#数据转化表达式，将表中列的一项较多的类转化1
mapok=map(change,dataframe.as_matrix())# 把数组框里的每一个元素进行转化
data=pda.DataFrame(list(mapok)).fillna(0)# 把数组里的其它空格项转化为0
# print(data)
# 临界支持度spt（俩者同时发生的概率），置信度设置cfd（在a条件下，b发生的概率）
spt=0.2 # 表示取大于0.2的关联项
cfd=0.5 # 表示取大于0.5的关联项
# 使用apriori算法计算关联结果

find_rule(data,spt,cfd,"-->")

