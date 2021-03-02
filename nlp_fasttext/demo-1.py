# coding:utf-8
from gensim.models import FastText

sentences = [["你", "是", "谁"], ["我", "是", "中国人"]]

model = FastText(sentences, size=4, window=3, min_count=1, iter=10, min_n=3, max_n=6, word_ngrams=0)
print(model['你'])  # 词向量获得的方式
print(model.wv['你'])  # 词向量获得的方式

'''
输出结果如下所示：
[-0.15942173 -0.12655328  0.00290119  0.0401443 ]
[-0.15942173 -0.12655328  0.00290119  0.0401443 ]
'''

'''
其中FastText主函数为：
class gensim.models.fasttext.FastText(sentences=None, corpus_file=None, sg=0, hs=0, size=100, alpha=0.025, window=5, min_count=5, max_vocab_size=None, word_ngrams=1, sample=0.001, seed=1, workers=3, min_alpha=0.0001, negative=5, ns_exponent=0.75, cbow_mean=1, hashfxn=<built-in function hash>, iter=5, null_word=0, min_n=3, max_n=6, sorted_vocab=1, bucket=2000000, trim_rule=None, batch_words=10000, callbacks=())


The commands supported by fasttext are:
 
  supervised              训练一个监督分类器
  quantize                量化模型以减少内存使用量
  test                    评估一个监督分类器
  predict                 预测最有可能的标签
  predict-prob            用概率预测最可能的标签
  skipgram                训练一个 skipgram 模型
  cbow                    训练一个 cbow 模型
  print-word-vectors      给定一个训练好的模型，打印出所有的单词向量
  print-sentence-vectors  给定一个训练好的模型，打印出所有的句子向量
  nn                      查询最近邻居
  analogies               查找所有同类词

'''

''' fasttext.supervised 参数如下
input_file                 训练文件路径（必须）
output                     输出文件路径（必须）
label_prefix               标签前缀 default __label__
lr                         学习率 default 0.1
lr_update_rate             学习率更新速率 default 100
dim                        词向量维度 default 100
ws                         上下文窗口大小 default 5
epoch                      epochs 数量 default 5
min_count                  最低词频 default 5
word_ngrams                n-gram 设置 default 1
loss                       损失函数 {ns,hs,softmax} default softmax
minn                       最小字符长度 default 0
maxn                       最大字符长度 default 0
thread                     线程数量 default 12
t                          采样阈值 default 0.0001
silent                     禁用 c++ 扩展日志输出 default 1
encoding                   指定 input_file 编码 default utf-8
pretrained_vectors         指定使用已有的词向量 .vec 文件 default None

'''