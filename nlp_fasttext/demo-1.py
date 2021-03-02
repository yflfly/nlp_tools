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

'''