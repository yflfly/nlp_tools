# coding:utf-8
from gensim import corpora, models
import jieba.posseg as jp
import jieba

# 基于LDA主题模型的关键词提取算法实现
# 简单文本处理
def get_text(text):
    flags = ('n', 'nr', 'ns', 'nt', 'eng', 'v', 'd')  # 词性
    stopwords = ('的', '就', '是', '用', '还', '在', '上', '作为')  # 停用词
    words_list = []
    for text in texts:
        words = [w.word for w in jp.cut(text) if w.flag in flags and w.word not in stopwords]
        words_list.append(words)
    return words_list


# 生成LDA模型
def LDA_model(words_list):
    # 构造词典
    # Dictionary()方法遍历所有的文本，为每个不重复的单词分配一个单独的整数ID，同时收集该单词出现次数以及相关的统计信息
    dictionary = corpora.Dictionary(words_list)
    print(dictionary)
    print('打印查看每个单词的id:')
    print(dictionary.token2id)  # 打印查看每个单词的id

    # 将dictionary转化为一个词袋
    # doc2bow()方法将dictionary转化为一个词袋。得到的结果corpus是一个向量的列表，向量的个数就是文档数。
    # 在每个文档向量中都包含一系列元组,元组的形式是（单词 ID，词频）
    corpus = [dictionary.doc2bow(words) for words in words_list]
    print('输出每个文档的向量:')
    print(corpus)  # 输出每个文档的向量

    # LDA主题模型
    # num_topics -- 必须，要生成的主题个数。
    # id2word    -- 必须，LdaModel类要求我们之前的dictionary把id都映射成为字符串。
    # passes     -- 可选，模型遍历语料库的次数。遍历的次数越多，模型越精确。但是对于非常大的语料库，遍历太多次会花费很长的时间。
    lda_model = models.ldamodel.LdaModel(corpus=corpus, num_topics=2, id2word=dictionary, passes=10)

    return lda_model


if __name__ == "__main__":
    texts = ['作为千元机中为数不多拥有真全面屏的手机，OPPO K3一经推出，就簇拥不少粉丝', \
             '很多人在冲着这块屏幕购买了OPPO K3之后，发现原来K3的过人之处不止是在屏幕上', \
             'OPPO K3的消费者对这部手机总体还是十分满意的', \
             '吉利博越PRO在7月3日全新吉客智能生态系统GKUI19发布会上正式亮相', \
             '今年上海车展，长安CS75 PLUS首次亮相', \
             '普通版车型采用的是双边共双出式排气布局；运动版本车型采用双边共四出的排气布局']
    # 获取分词后的文本列表
    words_list = get_text(texts)
    print('分词后的文本：')
    print(words_list)

    # 获取训练后的LDA模型
    lda_model = LDA_model(words_list)

    # 可以用 print_topic 和 print_topics 方法来查看主题
    # 打印所有主题，每个主题显示5个词
    topic_words = lda_model.print_topics(num_topics=2, num_words=5)
    print('打印所有主题，每个主题显示5个词:')
    print(topic_words)

    # 输出该主题的的词及其词的权重
    words_list = lda_model.show_topic(0, 5)
    print('输出该主题的的词及其词的权重:')
    print(words_list)

''''
运行显示如下所示：
Building prefix dict from the default dictionary ...
Dumping model to file cache C:\\Users\\think\AppData\Local\Temp\jieba.cache
Loading model cost 8.649 seconds.
Prefix dict has been built successfully.
分词后的文本：
[['拥有', '真', '全面', '手机', 'OPPO', 'K3', '一经', '推出', '簇拥', '不少', '粉丝'], ['人', '屏幕', '购买', 'OPPO', 'K3', '发现', '原来', 'K3', '不止', '屏幕'], ['OPPO', 'K3', '消费者', '部手机', '总体'], ['吉利', '博越', 'PRO', '全新', '吉客', '智能', 'GKUI19', '发布会', '亮相'], ['上海', '长安', 'CS75', 'PLUS', '亮相'], ['版', '车型', '采用', '双边', '共', '出式', '排气', '布局', '版本', '车型', '采用', '双边', '共', '排气', '布局']]
Dictionary(42 unique tokens: ['K3', 'OPPO', '一经', '不少', '全面']...)
打印查看每个单词的id:
{'K3': 0, 'OPPO': 1, '一经': 2, '不少': 3, '全面': 4, '手机': 5, '拥有': 6, '推出': 7, '真': 8, '簇拥': 9, '粉丝': 10, '不止': 11, '人': 12, '原来': 13, '发现': 14, '屏幕': 15, '购买': 16, '总体': 17, '消费者': 18, '部手机': 19, 'GKUI19': 20, 'PRO': 21, '亮相': 22, '全新': 23, '博越': 24, '发布会': 25, '吉利': 26, '吉客': 27, '智能': 28, 'CS75': 29, 'PLUS': 30, '上海': 31, '长安': 32, '共': 33, '出式': 34, '双边': 35, '布局': 36, '排气': 37, '版': 38, '版本': 39, '车型': 40, '采用': 41}
输出每个文档的向量:
[[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)], [(0, 2), (1, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 2), (16, 1)], [(0, 1), (1, 1), (17, 1), (18, 1), (19, 1)], [(20, 1), (21, 1), (22, 1), (23, 1), (24, 1), (25, 1), (26, 1), (27, 1), (28, 1)], [(22, 1), (29, 1), (30, 1), (31, 1), (32, 1)], [(33, 2), (34, 1), (35, 2), (36, 2), (37, 2), (38, 1), (39, 1), (40, 2), (41, 2)]]
打印所有主题，每个主题显示5个词:
[(0, '0.056*"K3" + 0.055*"屏幕" + 0.055*"亮相" + 0.034*"OPPO" + 0.033*"全新"'), (1, '0.048*"采用" + 0.048*"双边" + 0.048*"车型" + 0.048*"排气" + 0.048*"布局"')]
输出该主题的的词及其词的权重:
[('K3', 0.0563279), ('屏幕', 0.05533156), ('亮相', 0.055258993), ('OPPO', 0.033577614), ('全新', 0.033189856)]
'''
