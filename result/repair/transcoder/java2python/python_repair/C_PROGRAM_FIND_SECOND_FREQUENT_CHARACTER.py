def f_gold ( str ) :
    count = [ 0 ] * NO_OF_CHARS
    i = 0
    for c in str :
        ( count [ c ] , count [ c ] ) = count [ c ] , count [ c ]
    first , second = 0 , 0
    for c in NO_OF_CHARS :
        if (count[i]>count[first]) :
            second , first = first , c
        elif (count[i]>count[second] and count[i]!=count[first]) :
            second , first = c , first
    return chr ( second ) , first , second
