## 编辑距离


给定两个字符串S和T，对于T，我们允许三种操作：

1）在任意位置添加任意字符  batyu变为beatyu（插入字符e）

2）删除存在的任意字符  beatyu变为beaty（删除字符u）

3）修改任一字符  beauty变为beauti（将y变成i）

问最少操作多少次可以把字符串T变为S？

最少的操作次数，通常被称为编辑距离，即最短编辑距离。

安装：

pip install python-Levenshtein