

折腾,自己尝试写下自注意力算法.

​写了个最简易的transformer，但完全不明白输出应当是什么。以及要怎么优化参数。

2023 0526


我听说 qkv 三个权重矩阵是可学习的.但我不知道学习的算法,公式是什么.样本输入进来,我也不知道标签应该是什么.


transformer 简记 tsf 
我不觉得tsf一定要用于语言任务.它可以用于任意需求的特征提取.




win11
cuda117
miniconda3
python 39
torch 去官网查安装代码



softmax用法
https://cloud.tencent.com/developer/article/1725145



如果输入的矩阵(列向量的序列)是m行,n列
wq wk 必须 是 l行 m列
wv 可以是 j 行 m列

l j 是超参数,自行设定.


输出 的b 是j行 n列


c.ipynb
李沐的课件
帮忙理解注意力机制,但他明确说了,这里的内容没啥用.

230527