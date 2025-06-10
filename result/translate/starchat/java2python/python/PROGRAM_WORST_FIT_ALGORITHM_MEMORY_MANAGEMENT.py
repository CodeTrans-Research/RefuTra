def f_gold(block_size, m, process_size, n):
        allocation = [-1] * n
        for i in range(n):
            for j in range(m):
                if block_size[j] >= process_size[i]:
                    if wstIdx == -1:
                        wstIdx = j
                    elif blockSize[wstIdx] < blockSize[j]:
                        wstIdx = j
            if wstIdx!= -1:
                allocation[i] = wstIdx
                blockSize[wstIdx] -= process_size[i]
        print("Process No.\tProcess Size\tBlock no.")
        for i in range(n):
            print("   ", i+1, "\t\t", process_size[i], "\t\t", end='')
            if allocation[i]!= -1:
                print(allocation[i]+1, end='')
            else:
                print("Not Allocated")