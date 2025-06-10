def f_gold(str):
        len = len(str)
        res = [None] * len
        index = 0
        s = []
        for i in range(len):
            if str[i] == '+':
                if s[-1] == 1:
                    res[index] = '-'
                if s[-1] == 0:
                    res[index] = '+'
            elif str[i] == '-':
                if s[-1] == 1:
                    res[index] = '+'
                elif s[-1] == 0:
                    res[index] = '-'
            elif str[i] == '(':
                if i > 0 and str[i-1] == '-':
                    x = (s[-1] == 1)? 0 : 1
                    s.append(x)
                elif i > 0 and str[i-1] == '+':
                    s.append(s[-1])
            elif str[i] == ')':
                s.pop()
            else:
                res[index] = str[i]
            index += 1
        return ''.join(res)