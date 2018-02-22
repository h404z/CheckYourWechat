#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2018/2/22
# @Author: h404z

import itchat


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

    pass


if __name__ == '__main__':
    CYW().boys_and_girls
    pass
