def f_gold(s):
    if len(s) >= 10:
        return True
    for i in range(1, len(s)):
        for j in range(i+1, len(s)):
            for k in range(j+1, len(s)):
                s1, s2, s3, s4 = "", "", "", ""
                try:
                    s1 = s[:i]
                    s2 = s[i:j]
                    s3 = s[j:k]
                    s4 = s[k:]
                except:
                    pass
                if s1 != s2 and s1 != s3 and s1 != s4 and s2 != s3 and s2 != s4 and s3 != s4:
                    return True
    return False