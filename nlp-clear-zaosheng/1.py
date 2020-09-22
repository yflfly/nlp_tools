# coding:utf-8
import re


def clear_words(text):
    # remove html markup
    text = re.sub("(<.*?>)", "", text)

    # remove non-ascii and digits
    text = re.sub("(\W|\d)", "", text)

    # remove whitespace
    text = text.strip()

    return text


raw = ['..sleepy', 'sleepy!!', '#sleepy', '>>>>sleepy>>>>>', '<a>sleepy</a>', 'sleepy123', 's  leepy']

clear_res = [clear_words(each) for each in raw]
print(clear_res)

'''
输出结果如下所示：
['sleepy', 'sleepy', 'sleepy', 'sleepy', 'sleepy', 'sleepy', 'sleepy']
'''
