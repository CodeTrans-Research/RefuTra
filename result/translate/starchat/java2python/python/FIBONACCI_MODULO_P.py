def f_gold(p):
        first, second, number, next = 1, 1, 2, 1
        while next > 0:
            next = (first + second) % p
            first, second = second, next
            number += 1
        return number