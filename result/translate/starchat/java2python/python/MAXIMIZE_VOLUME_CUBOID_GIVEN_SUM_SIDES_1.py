def f_gold(s):
        length = s // 3
        s -= length * 3
        breadth = s // 2
        height = s - breadth
        return length * breadth * height