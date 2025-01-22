from setuptools import setup, find_packages

setup(
    name='FlowCls',    # import 什么就命名成什么
    version='0.1',    # 版本号
    packages=find_packages(),
    install_requires=[
        'torch==2.0.0',
        'numpy==1.24.0',
        'tqdm',
        'pillow',
        'torchvision==0.15.1'
    ],    # 把所有需要安装的包都写在这里
    author='sheqian',    # 作者
    description='Vit Flowers Classification',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sheqian36/FlowCls.git',    # 请修改为自己的github仓库地址
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)