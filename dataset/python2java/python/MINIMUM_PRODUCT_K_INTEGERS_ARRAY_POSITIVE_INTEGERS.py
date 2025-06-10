def f_gold(arr, n, k):
    pq = []
    for i in range(n):
        heapq.heappush(pq, arr[i])
    count = 0
    ans = 1
    while pq and count < k:
        ans += heapq.heappop(pq)
        count += 1
    return ans