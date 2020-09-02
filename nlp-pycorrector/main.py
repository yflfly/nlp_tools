# coding:utf-8
import pycorrector

# 文本纠错
correct, detail = pycorrector.correct("少先队员因该为老人让座")
print(correct, detail)

'''
输出结果为：
少先队员应该为老人让座 [[('因该', '应该', 4, 6)], [('坐', '座', 10, 11)]]
'''

# 错误检测
index_error = pycorrector.detect("少先队员因该为老人让座")
print(index_error)

'''
输出的结果为：
[['因该', 4, 6, 'word'], ['坐', 10, 11, 'char']]
返回类型是list, [error_word, begin_pos, end_pos, error_type]，pos索引位置以0开始。
'''

# 关闭字粒度纠错
error_sentence_1 = '我的喉咙发炎了要买点阿莫细林吃'
correct_sent = pycorrector.correct(error_sentence_1)
print(correct_sent)
'''
输出的结果为：
'我的喉咙发炎了要买点阿莫西林吉', [['细林', '西林', 12, 14], ['吃', '吉', 14, 15]]
例子“吃”发生了误纠，后续代码关闭字粒度纠错，代码如下所示
'''

error_sentence_1 = '我的喉咙发炎了要买点阿莫细林吃'
pycorrector.enable_char_error(enable=False)
correct_sent = pycorrector.correct(error_sentence_1)
print(correct_sent)

'''
输出的结果为：
'我的喉咙发炎了要买点阿莫西林吃', [['细林', '西林', 12, 14]]
'''