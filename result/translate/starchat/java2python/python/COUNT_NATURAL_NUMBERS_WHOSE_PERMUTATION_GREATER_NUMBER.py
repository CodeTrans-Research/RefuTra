def f_gold(n):
        result = 0
        for i in range(1, 10):
            stack = []
            if i <= n:
                stack.append(i)
                result += 1
            while stack:
                top = stack.pop()
                for j in range(top % 10, 10):
                    x = top * 10 + j
                    if x <= n:
                        stack.append(x)
                        result += 1
        return result