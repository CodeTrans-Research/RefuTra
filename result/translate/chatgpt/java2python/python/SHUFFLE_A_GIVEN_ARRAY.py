import random

def f_gold(arr, n):
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return arr