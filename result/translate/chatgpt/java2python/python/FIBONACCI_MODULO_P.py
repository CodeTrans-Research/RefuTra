def f_gold(p):
    first = 1
    second = 1
    number = 2
    next = 1
    while next > 0:
        next = (first + second) % p
        first = second
        second = next
        number += 1
    return number