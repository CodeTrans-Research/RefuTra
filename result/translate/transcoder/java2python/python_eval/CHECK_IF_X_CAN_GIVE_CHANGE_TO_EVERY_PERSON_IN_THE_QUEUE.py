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
def f_gold ( notes , n ) :
    fiveCount = 0
    tenCount = 0
    for i in range ( n ) :
        if ( notes [ i ] == 5 ) :
            fiveCount += 1
        elif ( notes [ i ] == 10 ) :
            if ( fiveCount > 0 ) :
                fiveCount -= 1
                tenCount += 1
            else :
                return 0
        else :
            if ( fiveCount > 0 and tenCount > 0 ) :
                fiveCount -= 1
                tenCount -= 1
            elif ( fiveCount >= 3 ) :
                fiveCount -= 3
            else :
                return 0
    return 1


def f_filled ( notes , n ) :
    five_count = 0
    ten_count = 0
    for i in range ( n ) :
        if notes [ i ] == 5 :
            five_count += 1
        elif notes [ i ] == 10 :
            if five_count > 0 :
                five_count -= 1
                ten_count += 1
            else :
                return 0
        else :
            if five_count > 0 and ten_count > 0 :
                five_count -= 1
                ten_count -= 1
            elif five_count >= 3 :
                five_count -= 3
            else :
                return 0
    return 1

if __name__ == '__main__':
    param = [
    ([5, 5, 5, 10, 20],4,),
    ([5,5,5,20,10],5,),
    ([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,10,10,10,10,10,10,10,10,10,10,10,10],27,),
    ([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,18],12,),
    ([5,5,20],2,),
    ([10,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],17,),
    ([5,10,20,5,5,5,5,5,5,5,5,5,5,5,5],7,),
    ([-82,-10,-78,-84,68,62,10,20,-86,-98,92,70,40,-12,-20,-36,8,-70,6,8,44,-24,8,-18,76,-54,-14,-94,-68,-62,-24,-36,-74,92,92,-80,48,56,94],31,),
    ([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],25,),
    ([46, 46, 93, 57, 82, 34, 83, 80, 77, 36, 80, 85, 69, 28, 9, 56, 49, 27, 83, 25, 1, 80, 99, 14, 69, 82, 79, 71, 74, 34],20,)
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
