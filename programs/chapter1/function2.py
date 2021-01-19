# -*- coding: utf-8 -*-
def fct1(*params_tpl):
    print(params_tpl)


fct1(1, 'a')         # => (1, 'a')


def fct2(**params_dic):
    print(params_dic)


fct2(p1=1, p2='a')   # => {'p2': 'a', 'p1': 1}