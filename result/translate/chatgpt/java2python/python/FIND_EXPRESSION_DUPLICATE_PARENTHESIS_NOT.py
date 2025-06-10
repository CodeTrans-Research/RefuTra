def f_gold(s):
    stack = []
    str = list(s)
    for ch in str:
        if ch == ')':
            top = stack[-1]
            stack.pop()
            elements_inside = 0
            while top != '(':
                elements_inside += 1
                top = stack[-1]
                stack.pop()
            if elements_inside < 1:
                return True
        else:
            stack.append(ch)
    return False