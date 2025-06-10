def f_gold(arr, n):
        ans = float("-inf")
        for i in range(n):
            curr_xor = 0
            for j in range(i, n):
                curr_xor = curr_xor ^ arr[j]
                ans = max(ans, curr_xor)
        return ans