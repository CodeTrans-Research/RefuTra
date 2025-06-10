def f_gold(s):
        stack = []
        for i in s:
            if i == ')':
                if not stack:
                    return False
                top = stack.pop()
                count = 0
                while top!= '(':
                    count += 1
                    top = stack.pop()
                if count < 1:
                    return True
            else:
                stack.append(i)
        return False