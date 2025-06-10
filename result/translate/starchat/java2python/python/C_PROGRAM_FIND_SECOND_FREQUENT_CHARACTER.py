def f_gold(str):
        count = [0] * 256
        for i in range(len(str)):
            count[ord(str[i])] += 1
        first, second = 0, 0
        for i in range(256):
            if count[i] > count[first]:
                second = first
                first = i
            elif count[i] > count[second] and count[i]!= count[first]:
                second = i
        return chr(second)