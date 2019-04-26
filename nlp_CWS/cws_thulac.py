#coding:utf-8

# 安装：pip install thulac
# 国内源安装：pip install thulac     -i https://pypi.tuna.tsinghua.edu.cn/simple
import thulac
# 默认模式：分词的同时进行词性标注
thulac_model = thulac.thulac()
result = thulac_model.cut("我愿做你的摆渡人，即使只能送你靠岸！")
print(result)

# 只进行分词
seg_only_model = thulac.thulac(seg_only=True)
result = seg_only_model.cut("我愿做你的摆渡人，即使只能送你靠岸！")
print(result)

'''
输出：
Model loaded succeed
[['我', 'r'], ['爱', 'v'], ['自然', 'n'], ['语言', 'n'], ['处理', 'v'], ['技术', 'n'], ['！', 'w']]
Model loaded succeed
[['我', ''], ['愿', ''], ['做', ''], ['你', ''], ['的', ''], ['摆渡', ''], ['人', ''], ['，', ''], ['即使', ''], ['只能', ''], ['送', ''], ['你', ''], ['靠岸', ''], ['！', '']]
'''