def f_gold(s):
        for i in range(len(s)):
            if not s[i].isdigit():
                return False
        return True