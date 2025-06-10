def f_gold(str, len):
        i = 0
        j = len - 1
        while i < j:
            if str[i] == str[j] and str[i]!= '*':
                i += 1
                j -= 1
            elif str[i] == str[j] and str[i] == '*':
                str[i] = 'a'
                str[j] = 'a'
                i += 1
                j -= 1
            elif str[i] == '*':
                str[i] = str[j]
                i += 1
            elif str[j] == '*':
                str[j] = str[i]
                j -= 1
            else:
                print("Not Possible")
                return ""
        return ''.join(str)