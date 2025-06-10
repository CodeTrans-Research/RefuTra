def f_gold(str1, str2):
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        res = ""
        n1 = len(str1)
        n2 = len(str2)
        str1 = str1[::-1]
        str2 = str2[::-1]
        carry = 0
        for i in range(n1):
            sum = (ord(str1[i]) - ord('0') + ord(str2[i]) - ord('0') + carry) % 10
            carry = (ord(str1[i]) - ord('0') + ord(str2[i]) - ord('0') + carry) // 10
            res = str(sum) + res
        for i in range(n1, n2):
            sum = (ord(str2[i]) - ord('0') + carry) % 10
            carry = (ord(str2[i]) - ord('0') + carry) // 10
            res = str(sum) + res
        if carry > 0:
            res = str(carry) + res