# coding:utf-8
# HanLP1.7.7版本
from pyhanlp import HanLP
from collections import Counter

with open("doc.txt", "r", encoding="utf-8-sig") as f:
    txt = f.read()

# 中国人名识别
nlp = HanLP.newSegment().enableNameRecognize(True)

# 地名识别
# nlp = HanLP.newSegment().enablePlaceRecognize(True)

# 机构名识别
# nlp = HanLP.newSegment().enableOrganizationRecognize(True)

doc = nlp.seg(txt)
c = Counter()
for w in doc:
    if w.toString().find("nr") >= 0:
        ww = w.toString()
    name = ww.split("/")[0]
    c[name] += 1
print(c.most_common(50))
