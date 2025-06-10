def f_gold(x):
        if x > 0:
            rightOne, nextHigherOneBit, rightOnesPattern, next = 0, 0, 0, 0
            rightOne = x & -x
            nextHigherOneBit = x + rightOne
            rightOnesPattern = x ^ nextHigherOneBit
            rightOnesPattern = rightOnesPattern >> 2
            next = nextHigherOneBit | rightOnesPattern
        return next