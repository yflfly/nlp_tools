# coding:utf-8
import jieba
import jieba.posseg as pseg
from DBSCAN_code import DBSCAN_View
import numpy as np


# 加载停用词表
def load_stopwords():
    # 从文件导入停用词表
    stpwrdpath = "stopwords.txt"
    stpwrd_dic = open(stpwrdpath, 'r', encoding='utf-8')
    stpwrd_content = stpwrd_dic.read()
    # 将停用词表转换为list
    stpwrdlst = stpwrd_content.splitlines()
    stpwrd_dic.close()

    return stpwrdlst


stopwords_list = load_stopwords()  # 加载停用词表


def read_data():
    # 去取txt文件中的内容，每一行存到List中，作为一个元素
    # 语料的基本预处理
    corpus = []
    with open('data_1.txt', encoding='utf-8') as fp:
        for line in fp.readlines():
            line = line.strip()
            if line == '':
                continue
            corpus.append(line.lower())
    return corpus


def get_weight():
    corpus = read_data()
    cutcorpusiter = corpus.copy()
    cutcorpus = corpus.copy()
    cixing_of_word = []  # 存储分词后的词语对应的词性
    word_to_cixing = []  # 存储分词后的词语
    for i in range(len(corpus)):
        cutcorpusiter[i] = pseg.cut(corpus[i])
        cutcorpus[i] = ''
        for every in cutcorpusiter[i]:
            cutcorpus[i] = (cutcorpus[i] + ' ' + str(every.word)).strip()
            cixing_of_word.append(every.flag)
            word_to_cixing.append(str(every.word))
    # 创建{词语：词性}的字典，方便后续使用词性
    word_flag_dict = {word_to_cixing[i]: cixing_of_word[i] for i in range(len(word_to_cixing))}
    '''
    在cutcorpus语料中，会存在“的”“了”等的停用词语，因为后续再进行特征提取时会按照词性进行权重赋值，所以这里并没有按照专用词和停用词词典进行筛选
    '''
    # 短文本特征提取

    from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf的权重
    # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(cutcorpus))
    # 获取词袋模型中的所有词语
    word = vectorizer.get_feature_names()
    # 将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    weight = tfidf.toarray()
    '''
    我们将word中每个词语的词性，通过自定义的方式赋给它们不同的权重，并乘到weight上的每一行样本中，进而改变它们的特征矩阵，这样做的目的其实是想让特征矩阵的区分能力增强一点
    '''
    wordflagweight = [1 for i in range(len(word))]  # 这个是词性系数，需要调整系数来看效果
    for i in range(len(word)):
        if str(word[i]) not in word_flag_dict:
            continue
        if (word_flag_dict[str(word[i])] == 'n'):  # 假设名词的词性重要一点，将系数给加大一点
            wordflagweight[i] = 1.2
        elif (word_flag_dict[str(word[i])] == 'vn'):
            wordflagweight[i] = 1.1
        elif (word_flag_dict[str(word[i])] == 'm'):  # 这里量词什么的直接去掉，省了一步停用词词典的去除
            wordflagweight[i] = 0
        elif (word_flag_dict[str(word[i])] == 'x'):
            wordflagweight[i] = 0
        else:
            continue  # 权重数值还要根据实际情况确定

    wordflagweight = np.array(wordflagweight)
    newweight = weight.copy()
    for i in range(len(weight)):
        for j in range(len(word)):
            newweight[i][j] = weight[i][j] * wordflagweight[j]

def write_cluster_to_file(labels_):
    # 将聚类的结果进行写入到文件
    import os
    import shutil
    shutil.rmtree('data_result') # 将上一次聚类的结果进行删除操作
    os.makedirs('data_result/') # 重新建立存储结果的文件夹

    corpus = read_data()
    for i in range(len(labels_)):
        with open('data_result/' + str(labels_[i]) + '.txt', 'a', encoding='utf-8') as fp:
            fp.write(corpus[i] + '\n')


# DBSCAN聚类
'''
sklearn三步走：调包、实例化、训练，DBSCAN有两个主要的参数需要调整，一个是eps(可以将它理解成聚类那个圈的半径)，一个是min_samples（最少多少个样本可以称之为一类），关于聚类效果的可视化，可以先将多维数据通过PCA压缩到聚类那么多维的数据，再通过TSN压缩到2维来描点作图，这样效果好点
'''
newweight = get_weight()
labels_, n_cluster = DBSCAN_View(1, 3, newweight)  # 返回值：索引号 簇的个数
write_cluster_to_file(labels_)
