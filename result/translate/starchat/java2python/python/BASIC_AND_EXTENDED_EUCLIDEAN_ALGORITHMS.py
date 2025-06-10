def f_gold(a: int, b: int) -> int:
        if a == 0:
            return b
        return f_gold(b % a, a)