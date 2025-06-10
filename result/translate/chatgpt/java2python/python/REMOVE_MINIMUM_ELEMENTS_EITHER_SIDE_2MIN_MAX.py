def f_gold(arr, n):
    longest_start = -1
    longest_end = 0
    
    for start in range(n):
        min_val = float('inf')
        max_val = float('-inf')
        
        for end in range(start, n):
            val = arr[end]
            
            if val < min_val:
                min_val = val
            if val > max_val:
                max_val = val
                
            if 2 * min_val <= max_val:
                break
                
            if end - start > longest_end - longest_start or longest_start == -1:
                longest_start = start
                longest_end = end
                
    if longest_start == -1:
        return n
    
    return n - (longest_end - longest_start + 1)