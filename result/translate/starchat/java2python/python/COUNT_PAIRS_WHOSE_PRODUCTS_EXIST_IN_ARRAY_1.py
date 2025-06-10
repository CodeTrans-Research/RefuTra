def f_gold(arr, n):
        result = 0
        hash_set = set()
        for i in range(n):
            hash_set.add(arr[i])
        for i in range(n):
            for j in range(i + 1, n):
                product = arr[i] * arr[j]
                if product in hash_set:
                    result += 1
        return result