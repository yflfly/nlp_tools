# coding:utf-8
from sklearn.cluster import DBSCAN
from sklearn import metrics  # 评估模型


def handle(labels, X_weight):
    # 计算噪声点个数的占总数的比例
    ratio = len(labels[labels[:] == -1]) / len(labels)
    print('噪声比：', format(ratio, '.2%'))

    # 获取分簇的数目
    n_cluster = len(set(labels)) - (1 if -1 in labels else 0)
    print('分簇的数目', n_cluster)

    # 轮廓系数评价聚类的好坏
    print("轮廓系数: %0.3f" % metrics.silhouette_score(X_weight, labels))

    return n_cluster


def DBSCAN_View(epsnumber, min_samplesnumber, X_weight):
    DBS_clf = DBSCAN(eps=epsnumber, min_samples=min_samplesnumber)  # DBSCAN聚类方法的调用
    DBS_clf.fit(X_weight)
    labels_ = DBS_clf.labels_  # 和X_weight同一个维度，labels对应的索引号的值为它所在簇的序号，若簇序号为-1，表示为噪声
    print(labels_, len(labels_), type(labels_))  # 打印每个样本的簇标好
    n_cluster = handle(labels_, X_weight)
    return labels_, n_cluster
