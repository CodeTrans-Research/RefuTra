def f_gold ( s ) :
    Stack = Stack ( )
    str = s.split ( )
    for ch in str :
        if ch == ')' :
            top = Stack.pop ( )
            Stack.pop ( )
            elementsInside = 0
            while top != '(' :
                elementsInside += 1
                top = Stack.pop ( )
                Stack.pop ( )
            if elementsInside < 1 :
                return True
        else :
            Stack.push ( ch )
    return False
