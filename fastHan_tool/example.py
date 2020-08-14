# coding:utf-8
from fastHan import FastHan

# 加载模型
model = FastHan(model_type='base')  # 用户首次初始化模型时模块将自动从服务器上下载参数，模型默认初始化 base 版本

# 输入句子
'''
输入模型的可以是单独的字符串，也可是由字符串组成的列表。
如果输入的是列表，模型将一次性处理所有输入的字符串，所以请自行控制 batch size。
模型对句子进行依存分析、命名实体识别的简单例子如下：
'''
sentences = ["我爱踢足球。", "林丹是冠军"]
#
answer = model(sentences, 'Parsing')
for i, sentence in enumerate(answer):
    print(i)
    for token in sentence:
        print(token, token.pos, token.head, token.head_label)
''''
运行结果如下所示：
0
我 PN 2 nsubj
爱 VV 0 root
踢 VV 2 ccomp
足球 NN 3 dobj
。 PU 2 punct

1
林丹 NR 2 top
是 VC 0 root
冠军 NN 2 attr
'''


