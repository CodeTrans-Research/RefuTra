def f_gold(l):
    leafNodeCount = 2 ** (l - 1)
    sumLastLevel = 0
    sumLastLevel = (leafNodeCount * (leafNodeCount + 1)) / 2
    sum = sumLastLevel * l
    return sum