def f_gold(arr, n):
    evenArr = []
    oddArr = []
    
    for i in range(n):
        if i % 2 != 1:
            evenArr.append(arr[i])
        else:
            oddArr.append(arr[i])
    
    evenArr.sort()
    oddArr.sort(reverse=True)
    
    i = 0
    for j in range(len(evenArr)):
        arr[i] = evenArr[j]
        i += 1
    
    for j in range(len(oddArr)):
        arr[i] = oddArr[j]
        i += 1