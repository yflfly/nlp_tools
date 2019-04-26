#coding:utf-8

#  安装 pip install jieba
# 国内安装更快的方式：pip install jieba -i https://pypi.tuna.tsinghua.edu.cn/simple

import jieba

# 全模式
result = jieba.cut("我愿做你的摆渡人，即使只能送你靠岸", cut_all=True)
print(" ".join(result))

# 精确模式
result = jieba.cut("我愿做你的摆渡人，即使只能送你靠岸！", cut_all=False)
print(" ".join(result))

# 搜索引擎模式
result = jieba.cut_for_search("我愿做你的摆渡人，即使只能送你靠岸！")
print(" ".join(result))

'''
我 愿 做 你 的 摆渡 摆渡人   即使 只能 送 你 靠岸
我愿 做 你 的 摆渡人 ， 即使 只能 送 你 靠岸 ！
我愿 做 你 的 摆渡 摆渡人 ， 即使 只能 送 你 靠岸 ！
'''