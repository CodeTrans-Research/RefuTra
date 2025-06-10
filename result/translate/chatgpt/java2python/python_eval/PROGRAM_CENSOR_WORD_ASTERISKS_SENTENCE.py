import sys
import math
import heapq
from queue import Queue
import numpy as np
# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( text , word ) :
    word_list = text.split ( )
    result = ''
    stars = '*' * len ( word )
    count = 0
    index = 0 ;
    for i in word_list :
        if i == word :
            word_list [ index ] = stars
        index += 1
    result = ' '.join ( word_list )
    return result


def f_filled(text, word):
    word_list = text.split()
    result = ""
    stars = ""
    for i in range(len(word)):
        stars += '*'
    index = 0
    for i in range(len(word_list)):
        if word_list[i] == word:
            word_list[i] = stars
    for i in word_list:
        result += i + ' '
    return result

if __name__ == '__main__':
    param = [
    ('IggvAXtmJ','kzHdEJuCaO',),
    ('76711241128','5',),
    ('010','0101001',),
    ('HIKOn','XlnBwpx',),
    ('3680369217','017523',),
    ('1111','1011',),
    ('zIi','ONNXygON',),
    ('06','54171617',),
    ('111','0010001011001',),
    ('NJNnrVU','AGwmS',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        import copy
        p2 = copy.deepcopy(parameters_set)
        filledres = f_filled(*parameters_set)
        goldres = f_gold(*p2)
        if filledres == goldres:
            n_success+=1
        else:
            if set([filledres,goldres]) <= set([float("inf"),sys.maxsize,2147483647]) or set([filledres,goldres]) <= set([float("-inf"),-sys.maxsize-1,-sys.maxsize,-2147483648]):
                n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
