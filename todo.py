# -*- coding: utf-8 -*-
# 简单计算器 v2.0（分支开发中）
# 功能：加法、减法、乘法

def add(a, b):
    """返回两个数的和"""
    return a + b

def subtract(a, b):
    """返回两个数的差"""
    return a - b

def multiply(a, b):  # 新添加的乘法功能
    """返回两个数的积"""
    return a * b

if __name__ == "__main__":
    # 使用 format() 方法替代 f-string，兼容 Python 3.5 及以下版本
    print("3 + 5 = {}".format(add(3, 5)))
    print("10 - 4 = {}".format(subtract(10, 4)))
    print("6 × 7 = {}".format(multiply(6, 7)))  # 测试乘法

    111
