import sys
import math
import heapq
from queue import Queue
# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( string ) :
    Stack = [ ]
    for ch in string :
        if ch == ')' :
            top = Stack.pop ( )
            elementsInside = 0
            while top != '(' :
                elementsInside += 1
                top = Stack.pop ( )
            if elementsInside < 1 :
                return True
        else :
            Stack.append ( ch )
    return False


def f_filled(s):
    stack = []
    str = list(s)
    for ch in str:
        if ch == ')':
            top = stack[-1]
            stack.pop()
            elements_inside = 0
            while top != '(':
                elements_inside += 1
                top = stack[-1]
                stack.pop()
            if elements_inside < 1:
                return True
        else:
            stack.append(ch)
    return False

if __name__ == '__main__':
    param = [
    ("((a+b)+((c+d)))",),
    ("(((a+(b)))+(c+d))",),
    ("(((a+(b))+c+d))",),
    ("((a+b)+(c+d))",),
    ("(8582007)",),
    ("((a+(b))+(c+d))",),
    ("(PylsShEdKAE)",),
    ('886980680541',),
    ('001',),
    ('jsVmFeOq',)
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
            if set([filledres,goldres]) == set([float("inf"),sys.maxsize]) or set([filledres,goldres]) <= set([float("-inf"),-sys.maxsize-1,-sys.maxsize]):
                n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
