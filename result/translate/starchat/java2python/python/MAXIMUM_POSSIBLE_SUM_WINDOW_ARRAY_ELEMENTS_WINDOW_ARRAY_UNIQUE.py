def f_gold(A, B, n):
        mp = set()
        result = 0
        curr_sum = 0
        curr_begin = 0
        for i in range(n):
            while A[curr_begin] in mp:
                mp.remove(A[curr_begin])
                curr_sum -= B[curr_begin]
                curr_begin += 1
            mp.add(A[i])
            curr_sum += B[i]
            result = max(result, curr_sum)
        return result