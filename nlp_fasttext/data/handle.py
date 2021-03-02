# coding:utf-8
import jieba

zhifulei = []
with open('支付类.txt', encoding='utf-8') as fp:
    for line in fp.readlines():
        line = line.strip()
        if line == '':
            continue
        zhifulei.append(' '.join(jieba.cut(line)))

danbaolei = []
with open('担保类.txt', encoding='utf-8') as fp:
    for line in fp.readlines():
        line = line.strip()
        if line == '':
            continue
        danbaolei.append(' '.join(jieba.cut(line)))

chouzilei = []
with open('筹资类.txt', encoding='utf-8') as fp:
    for line in fp.readlines():
        line = line.strip()
        if line == '':
            continue
        print(' '.join(jieba.cut(line)))
        chouzilei.append(' '.join(jieba.cut(line)))

print(len(zhifulei), len(danbaolei), len(chouzilei))

with open('data.txt', 'w', encoding='utf-8') as fp:
    for line in zhifulei:
        fp.write('支付类	1	'+line+'\n')
    for line in danbaolei:
        fp.write('担保类	2	'+line+'\n')
    for line in chouzilei:
        fp.write('筹资类	3	'+line+'\n')
