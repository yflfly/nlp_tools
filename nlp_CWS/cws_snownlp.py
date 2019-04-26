#coding:utf-8
# 安装：pip install snownlp
# 国内源安装：pip install snownlp  -i https://pypi.tuna.tsinghua.edu.cn/simple

import snownlp
from snownlp import SnowNLP
result = SnowNLP(u'我愿做你的摆渡人，即使只能送你靠岸！')
print(result.words)

'''
输出：
['我', '愿', '做', '你', '的', '摆渡', '人', '，', '即使', '只', '能', '送', '你', '靠岸', '！']
'''
