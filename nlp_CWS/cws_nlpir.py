#coding:utf-8
# 安装：pip install pynlpir
# 国内源安装：pip install pynlpir -i https://pypi.tuna.tsinghua.edu.cn/simple
# 导入pynlpir包
# 如果发现加载报错，则需要更换license：https://github.com/NLPIR-team/NLPIR/tree/master/License/
import pynlpir
# 打开分词器
pynlpir.open()
# 分词：这个工具会同时进行词性标注
s = "我愿做你的摆渡人，即使只能送你靠岸！"
result = pynlpir.segment(s)
print(result)

'''
输出：
[('我', 'pronoun'), ('愿', 'verb'), ('做', 'verb'), ('你', 'pronoun'), ('的', 'particle'), ('摆渡', 'noun'), ('人', 'noun'), ('，', 'punctuation mark'), ('即使', 'conjunction'), ('只能', 'verb'), ('送', 'verb'), ('你', 'pronoun'), ('靠岸', 'verb'), ('！', 'punctuation mark')]
'''
