def f_gold(str):
    len_str = len(str)
    res = [''] * len_str
    index = 0
    i = 0
    s = []
    s.append(0)
    
    while i < len_str:
        if str[i] == '+':
            if s[-1] == 1:
                res[index] = '-'
                index += 1
            if s[-1] == 0:
                res[index] = '+'
                index += 1
        elif str[i] == '-':
            if s[-1] == 1:
                res[index] = '+'
                index += 1
            elif s[-1] == 0:
                res[index] = '-'
                index += 1
        elif str[i] == '(' and i > 0:
            if str[i - 1] == '-':
                x = 0 if s[-1] == 1 else 1
                s.append(x)
            elif str[i - 1] == '+':
                s.append(s[-1])
        elif str[i] == ')':
            s.pop()
        else:
            res[index] = str[i]
            index += 1
        i += 1
        
    return ''.join(res)