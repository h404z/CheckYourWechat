#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2018/2/22
# @Author: h404z

import itchat
import re
import numpy
import PIL
import wordcloud


class CYW(object):
    def __init__(self):
        itchat.login()
        self.friends = itchat.get_friends(update=True)[0:]
        pass

    @property
    def boys_and_girls(self):
        """统计自己wechat好友中的那男女比例"""
        boys = girls = other = 0
        for fri in self.friends:
            if fri['Sex'] == 1:
                boys += 1
            elif fri['Sex'] == 0:
                girls += 1
            else:
                other += 1
        total = len(self.friends)
        print('男生人数：{}， 占总人数的{:%}%'.format(boys, round(boys / total, 2)))
        print('女生人数：{}， 占总人数的{:%}%'.format(girls, round(girls / total, 2)))
        print('不明性别人数：{}， 占总人数的{:%}%'.format(other, round(other / total, 2)))
        return {'boys': boys, 'girls': girls, 'other': other}

    def analyse_signature(self):
        """分析好友签名特征"""

        def clean_signatrure():
            """
            很多本来是表情的，变成了emoji、span、class等等这些无关紧要的词，需要先替换掉，
            另外，还有类似<>/= 之类的符号，也需要写个简单的正则替换掉，再把所有拼起来，得到text字串
            """
            pass

        def extract_signature():
            """用jieba分词提取"""
            pass

        sig_list = []
        # todo: 继续完成好友签名分析功能

        pass

    pass


if __name__ == '__main__':
    CYW().boys_and_girls
    pass
