#!/usr/bin/env python
# coding=utf-8

# 打包的用的setup必须引入


from setuptools import setup

VERSION = '0.1'

with open('README.md') as f:
    long_description = f.read()

setup(
    name='threshold',                                                  # 文件名
    version=VERSION,                                                   # 版本(每次更新上传Pypi需要修改)
    description="a simple param filter for web framework by Python",   # 描述
    long_description=long_description,                                 # 放README.md文件,方便在Pypi页展示
    classifiers=[],
    keywords='python threshold argument filter',                       # 关键字
    author='BingLau',                                                  # 用户名
    author_email='binglau1819@gmail.com',                              # 邮箱
    url='https://github.com/BingLau7/Threshold',                       # github 上的地址,别的地址也可以
    license='MIT',                                                     # 遵循的协议
    packages=['threshold'],                                            # 发布的包名
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'termcolor',
    ],                                                                 # 满足的依赖
)
