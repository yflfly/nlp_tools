# coding:utf-8
import Levenshtein

str1 = u'自然语言处理'
str2 = u'自然语言处理'
str3 = u'然语言处理NLP'
print(Levenshtein.distance(str1, str2))
print(Levenshtein.distance(str1, str3))
