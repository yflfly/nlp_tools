# coding:utf-8
import fasttext.FastText as ff

# classifier = fasttext.supervised('mi/data.txt', 'classifier.model', label_prefix='__label__', min_count=1,
#                                  word_ngrams=2, bucket=2000000, lr=0.1, epoch=10, dim=200)

classifier = ff.train_supervised("mi/data.txt")
model = classifier.save_model('mi/try.model')  # 保存模型
test = classifier.test('mi/test.txt')  # 输出测试结果
print(classifier.get_labels())  # 输出标签
pre = classifier.predict('文本')  # 输出改文本的预测结

print(pre)