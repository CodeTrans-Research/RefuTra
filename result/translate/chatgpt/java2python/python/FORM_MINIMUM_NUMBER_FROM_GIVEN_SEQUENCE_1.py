def f_gold(seq):
    n = len(seq)
    if n >= 9:
        return "-1"
    result = [''] * (n + 1)
    count = 1
    i = 0
    while i <= n:
        if i == n or seq[i] == 'I':
            j = i - 1
            while j >= -1:
                result[j + 1] = chr(ord('0') + count)
                count += 1
                if j >= 0 and seq[j] == 'I':
                    break
                j -= 1
        i += 1
    return ''.join(result)