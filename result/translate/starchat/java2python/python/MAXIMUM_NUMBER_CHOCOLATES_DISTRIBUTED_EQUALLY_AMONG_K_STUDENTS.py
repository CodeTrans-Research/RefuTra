def f_gold(arr, n, k):
        sum_arr = [0] * (n)
        sum_arr[0] = arr[0]
        for i in range(1, n):
            sum_arr[i] = sum_arr[i - 1] + arr[i]
        um = {}
        max_sum = 0
        for i in range(n):
            curr_rem = sum_arr[i] % k
            if curr_rem == 0:
                if max_sum < sum_arr[i]:
                    max_sum = sum_arr[i]
            else:
                if curr_rem not in um:
                    um[curr_rem] = i
                else:
                    if max_sum < (sum_arr[i] - sum_arr[um[curr_rem]]):
                        max_sum = sum_arr[i] - sum_arr[um[curr_rem]]
        return max_sum // k