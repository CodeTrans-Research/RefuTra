public static int f_gold(int input, int unlock_code) {
    int rotation = 0;
    while (input > 0 || unlock_code > 0) {
        int input_digit = input % 10;
        int code_digit = unlock_code % 10;
        rotation += Math.min(Math.abs(input_digit - code_digit), 10 - Math.abs(input_digit - code_digit));
        input = input / 10;
        unlock_code = unlock_code / 10;
    }
    return rotation;
}