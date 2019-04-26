#coding:utf-8
# 安装：pip install pyhanlp
# 国内源安装：pip install pyhanlp  -i https://pypi.tuna.tsinghua.edu.cn/simple
from pyhanlp import *

s = '我愿做你的摆渡人，即使只能送你靠岸！'
result = HanLP.segment(s)
for each in result:
   print(each.word)

'''
输出：

'''
