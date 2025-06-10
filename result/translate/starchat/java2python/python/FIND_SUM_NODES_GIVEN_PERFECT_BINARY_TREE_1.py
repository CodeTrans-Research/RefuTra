def f_gold(l):
        leafNodeCount = math.pow(2, l - 1)
        sumLastLevel = (leafNodeCount * (leafNodeCount + 1)) / 2
        sum = sumLastLevel * l
        return sum