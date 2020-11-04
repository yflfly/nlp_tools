## TF-IDF

TF-IDF是一种基于频率的方法，它考虑了单词在语料库中出现的频率。

这是一种表示给定文档中特定单词的重要性的单词表示。直观地说，单词的频率越高，该单词在文档中就越重要。

例如，在关于猫的文档中，单词cats会出现更多次。然而，仅仅计算频率是行不通的，因为像this和is这样的词是非常频繁的，但是它们并没有携带很多信息。TF-IDF将此考虑在内，并把这些常用单词的值置为零。

同样，TF代表词频率，IDF代表逆文档频率：
![Image text](https://github.com/yflfly/nlp_tools/tree/master/nlp-TFIDF/image/1.jpg)


下面做个快速练习，考虑两个文件：

● 文件1:This is about cats. Cats are great companions.

● 文件2:This is about dogs. Dogs are very loyal.

现在让我们来处理一些数字：

TF-IDF(cats,doc1)=(2/8)*log(2/1)=0.075

TF-IDF(this,doc2)=(1/8)*log(2/2)=0.0

因此，cat这个词具有丰富的信息，而this这个词不是，这是我们在衡量单词重要性方面所期望的行为。