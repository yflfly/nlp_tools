#coding:utf-8
import nltk
from nltk.corpus import wordnet as wn
for synset in wn.synsets(u'计算机', lang='cmn'):
    for lemma in synset.lemma_names('cmn'):
        print(lemma)
