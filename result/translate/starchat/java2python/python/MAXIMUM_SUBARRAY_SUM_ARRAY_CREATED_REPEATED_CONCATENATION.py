def f_gold(a, n, k):
        max_so_far = 0
        INT_MIN = sys.maxsize
        max_ending_here = 0
        for i in range(0, n * k):
            max_ending_here = max_ending_here + a[i % n]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far