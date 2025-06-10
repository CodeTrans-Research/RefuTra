def f_gold(x):
    rightOne = 0
    nextHigherOneBit = 0
    rightOnesPattern = 0
    next = 0

    if x > 0:
        rightOne = x & -x
        nextHigherOneBit = x + rightOne
        rightOnesPattern = x ^ nextHigherOneBit
        rightOnesPattern = (rightOnesPattern) // rightOne
        rightOnesPattern >>= 2
        next = nextHigherOneBit | rightOnesPattern

    return next