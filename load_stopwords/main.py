#coding:utf-8

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
stopwords = load_stopwords()
for word in stopwords:
    print(word)