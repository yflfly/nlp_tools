# coding:utf-8
from textblob import TextBlob

text = 'I am happy today. I feel sad today'
blob = TextBlob(text)
# 分句
blob = blob.sentences
print(blob)

# 第一句的情感分析
first = blob.sentences[0].sentiment
print(first)
# 第二句的情感分析
second = blob.sentences[1].sentiment
print(second)
# 总的
all = blob.sentiment
