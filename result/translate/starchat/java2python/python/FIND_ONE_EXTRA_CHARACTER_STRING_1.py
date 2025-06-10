def f_gold(strA, strB):
        res = 0
        for i in range(len(strA)):
            res ^= ord(strA[i])
        for i in range(len(strB)):
            res ^= ord(strB[i])
        return chr(res)