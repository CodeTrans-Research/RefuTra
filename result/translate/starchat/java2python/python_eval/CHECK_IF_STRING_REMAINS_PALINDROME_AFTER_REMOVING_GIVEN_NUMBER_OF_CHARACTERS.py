import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( str , n ) :
    l = len ( str )
    if ( l >= n ) :
        return True
    return False


def f_filled(str, n):
        return len(str) >= n

if __name__ == '__main__':
    param = [
    ('ZCoQhuM',2,),
    ('7437725',53,),
    ('11',30,),
    ('buGlvR',1,),
    ('9',92,),
    ('101101010110',3,),
    ('YguiM',18,),
    ('8198',90,),
    ('11101',71,),
    ('hUInqJXNdbfP',4,)
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
