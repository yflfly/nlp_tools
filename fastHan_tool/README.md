# FastHan

## 介绍
```
fastHan 是基于 fastNLP 与 PyTorch 实现的中文自然语言处理工具，像 spacy 一样调用方便，其内核为基于 BERT 的联合模型。简介
fastHan 是基于 fastNLP 与 PyTorch 实现的中文自然语言处理工具，像 spacy 一样调用方便。其内核为基于 BERT 的联合模型，其在 13 个语料库中进行训练，可处理中文分词、词性标注、依存句法分析、命名实体识别四项任务。
fastHan 共有 base 与 large 两个版本，分别利用 BERT 的前四层与前八层。base 版本在总参数量 150MB 的情况下各项任务均有不错表现，large 版本则接近甚至超越 SOTA 模型。
```