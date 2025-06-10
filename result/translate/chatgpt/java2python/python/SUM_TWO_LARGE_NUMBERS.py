def f_gold(str1, str2):
    if len(str1) > len(str2):
        t = str1
        str1 = str2
        str2 = t

    str = ""
    n1 = len(str1)
    n2 = len(str2)

    str1 = str1[::-1]
    str2 = str2[::-1]

    carry = 0
    for i in range(n1):
        sum = (int(str1[i]) - int('0')) + (int(str2[i]) - int('0')) + carry
        str += chr(sum % 10 + int('0'))
        carry = sum // 10

    for i in range(n1, n2):
        sum = (int(str2[i]) - int('0')) + carry
        str += chr(sum % 10 + int('0'))
        carry = sum // 10

    if carry != 0:
        str += chr(carry + int('0'))

    str = str[::-1]
    return str