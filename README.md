# 第八节：深度学习常见模型
this is a pytorch deep learning project for the five flowers' classification project with ViT(vision_transformer).

这是一个基于ViT的花朵图像分类的pytorch深度学习项目。

# 安装

环境：

```python
conda create -n flowcls python=3.10
```

```
pip install git+https://github.com/sheqian36/FlowCls.git
```
or
```
git clone https://github.com/sheqian36/FlowCls.git
cd FlowCls
pip install -e .
```
# 权重加载

把预训练权重 model-9.pth 放到 ./FlowCls/models 目录 （需要新建 models 目录） 下即可

权重下载：[百度网盘](https://pan.baidu.com/s/1VRe2e2coJwK8pND4zqGoRQ?pwd=mixv) (提取码：mixv) 或 [谷歌网盘](https://drive.google.com/file/d/1o4VaL0ABk8_1i_EorR3P07YJk8GCjYAl/view?usp=sharing)

# 使用示例
```
python demo.py
```
