def f_gold(n, templeHeight):
    sum = 0
    for i in range(n):
        left = 0
        right = 0
        j = i - 1
        while j >= 0:
            if templeHeight[j] < templeHeight[j + 1]:
                left += 1
            else:
                break
            j -= 1
        
        j = i + 1
        while j < n:
            if templeHeight[j] < templeHeight[j - 1]:
                right += 1
            else:
                break
            j += 1
        
        sum += max(right, left) + 1
        
    return sum