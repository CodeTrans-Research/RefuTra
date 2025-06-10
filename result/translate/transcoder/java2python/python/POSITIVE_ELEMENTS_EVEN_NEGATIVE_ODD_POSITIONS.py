def f_gold ( a , size ) :
    positive , negative , temp = 0 , 1 , 0
    while True :
        while positive < size and a [ positive ] >= 0 :
            positive += 2
        while negative < size and a [ negative ] <= 0 :
            negative += 2
        if positive < size and negative < size :
            temp = a [ positive ]
            a [ positive ] , a [ negative ] = a [ negative ] , temp
        else :
            break
