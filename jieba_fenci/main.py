# coding:utf-8
import jieba


# 对一句话进行分词
def handle_1():
    string = '自然语言处理NLP'
    # jieba.cut直接得到generator形式的分词结果
    seg = jieba.cut(string)
    print(' '.join(seg))

    # 也可以使用jieba.lcut得到list的分词结果
    seg = jieba.lcut(string)
    print(seg)
    '''
    运行的结果如下所示：
    自然语言 处理 NLP
    ['自然语言', '处理', 'NLP']
    '''


# 词性分析
import jieba.posseg as pos


def handle_2():
    string = '自然语言处理NLP'
    # generator形式形如pair(‘word’, ‘pos’)的结果
    seg = pos.cut(string)
    print([se for se in seg])

    # list形式的结果
    seg = pos.lcut(string)
    print(seg)
    '''
    运行的结果如下所示：
    [pair('自然语言', 'l'), pair('处理', 'v'), pair('NLP', 'eng')]
    [pair('自然语言', 'l'), pair('处理', 'v'), pair('NLP', 'eng')]
    '''
