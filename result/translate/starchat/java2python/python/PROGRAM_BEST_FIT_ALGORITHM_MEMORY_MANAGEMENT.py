def f_gold(block_size, m, process_size, n):
        allocation = [-1] * n
        for i in range(n):
            best_idx = -1
            for j in range(m):
                if block_size[j] >= process_size[i]:
                    if best_idx == -1:
                        best_idx = j
                    elif block_size[best_idx] > block_size[j]:
                        best_idx = j
            if best_idx!= -1:
                allocation[i] = best_idx
                block_size[best_idx] -= process_size[i]
        print("Process No.\tProcess Size\tBlock no.")
        for i in range(n):
            print("   ", i + 1, "\t\t", process_size[i], "\t\t",
                  allocation[i] if allocation[i]!= -1 else "Not Allocated")