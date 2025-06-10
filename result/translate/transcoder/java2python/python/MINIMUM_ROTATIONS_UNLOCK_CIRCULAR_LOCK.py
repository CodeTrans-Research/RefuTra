def f_gold ( input , unlock_code ) :
    rotation = 0
    input_digit , code_digit = input
    while input or unlock_code :
        input_digit = input % 10
        code_digit = unlock_code % 10
        rotation += min ( abs ( input_digit - code_digit ) , 10 - abs ( input_digit - code_digit ) )
        input /= 10
        unlock_code /= 10
    return rotation
