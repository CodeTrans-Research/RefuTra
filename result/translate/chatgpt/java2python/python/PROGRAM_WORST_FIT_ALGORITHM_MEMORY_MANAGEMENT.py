def f_gold(blockSize, m, processSize, n):
    allocation = [-1] * n
    for i in range(n):
        wstIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if wstIdx == -1:
                    wstIdx = j
                elif blockSize[wstIdx] < blockSize[j]:
                    wstIdx = j
        if wstIdx != -1:
            allocation[i] = wstIdx
            blockSize[wstIdx] -= processSize[i]

    print("\nProcess No.\tProcess Size\tBlock no.")
    for i in range(n):
        print("  " + str(i + 1) + "\t\t" + str(processSize[i]) + "\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")
        print()