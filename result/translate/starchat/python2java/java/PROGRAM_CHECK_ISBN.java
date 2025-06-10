public static boolean f_gold ( String isbn ) {
    if (isbn.length()!= 10) return false;
    int sum = 0;
    for (int i = 0; i < 9; i++) {
        if (isbn.charAt(i) >= '0' && isbn.charAt(i) <= '9')
            sum += (isbn.charAt(i) - '0') * (10 - i);
        else
            return false;
    }
    if (isbn.charAt(9) == 'X') sum += 10;
    else if (isbn.charAt(9) >= '0' && isbn.charAt(9) <= '9') sum += (isbn.charAt(9) - '0');
    else return false;
    return (sum % 11 == 0);
}