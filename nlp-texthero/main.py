# coding:utf-8
import pandas as pd
import texthero as hero

"""简单的文本清理管道"""
# 显示所有的行列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)
text = "视频中的表演者何维越在接受澎湃新闻记者采访时表示，这段“武术表演”其实是为了讽刺那些招摇撞骗的假大师，他自己其实是传统武术爱好者。此前，他已经做过许多类似的反讽表演。（12306/）！"
# 格式化为series格式
s = pd.Series(text)
print(s)  # This sèntencé    (123 /) needs to [OK!] be cleaned!
# 去掉了数字
s = hero.remove_digits(s)
print(s)  # This sèntencé    (  /) needs to [OK!] be cleaned!
# 删除所有类型的括号及其内容
s = hero.remove_brackets(s)
print(s)
# 删除变音符号即声标
s = hero.remove_diacritics(s)
print(s)
# 删除标点符号。
s = hero.remove_punctuation(s)
print(s)
# 删除多余的空格。
s = hero.remove_whitespace(s)
print(s)

# 停用词,无意义的词
s = hero.remove_stopwords(s)
print(s)

# nlp提取名词
s = hero.named_entities(s)
print("nlp:", s)

s = hero.noun_chunks(s)
print(s)

'''
输出结果如下所示：
0    视频中的表演者何维越在接受澎湃新闻记者采访时表示，这段“武术表演”其实是为了讽刺那些招摇撞骗的假大师，他自己其实是传统武术爱好者。此前，他已经做过许多类似的反讽表演。（12306/）！
dtype: object
0    视频中的表演者何维越在接受澎湃新闻记者采访时表示，这段“武术表演”其实是为了讽刺那些招摇撞骗的假大师，他自己其实是传统武术爱好者。此前，他已经做过许多类似的反讽表演。（ /）！
dtype: object
0    视频中的表演者何维越在接受澎湃新闻记者采访时表示，这段“武术表演”其实是为了讽刺那些招摇撞骗的假大师，他自己其实是传统武术爱好者。此前，他已经做过许多类似的反讽表演。（ /）！
dtype: object
0    Shi Pin Zhong De Biao Yan Zhe He Wei Yue Zai Jie Shou Peng Pai Xin Wen Ji Zhe Cai Fang Shi Biao ...
dtype: object
0    Shi Pin Zhong De Biao Yan Zhe He Wei Yue Zai Jie Shou Peng Pai Xin Wen Ji Zhe Cai Fang Shi Biao ...
dtype: object
0    Shi Pin Zhong De Biao Yan Zhe He Wei Yue Zai Jie Shou Peng Pai Xin Wen Ji Zhe Cai Fang Shi Biao ...
dtype: object
0    Shi Pin Zhong De Biao Yan Zhe He Wei Yue Zai Jie Shou Peng Pai Xin Wen Ji Zhe Cai Fang Shi Biao ...
dtype: object
nlp: 0    [(Shi Pin, PERSON, 0, 7), (Zhong De, PERSON, 8, 16), (Yan Zhe, PERSON, 22, 29), (Wei Yue Zai Jie...
dtype: object
0    [([('Shi Pin', 'PERSON, NP, 0, 20), (Zhong De, NP, 32, 40), ('PERSON, NP, 43, 50), (('Yan Zhe, N...
dtype: object

'''