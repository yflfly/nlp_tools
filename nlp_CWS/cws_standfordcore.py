#coding:utf-8
# 安装：pip install stanfordcorenlp
# 国内源安装：pip install stanfordcorenlp -i https://pypi.tuna.tsinghua.edu.cn/simple
from stanfordcorenlp import StanfordCoreNLP
# 先下载模型，然后导入,下载地址：https://nlp.stanford.edu/software/

nlp_model = StanfordCoreNLP(r'stanford-corenlp-full-2018-02-27', lang='zh')
# 分词
s = '我愿做你的摆渡人，即使只能送你靠岸！！'
result = nlp_model.word_tokenize(s)
print(result)
