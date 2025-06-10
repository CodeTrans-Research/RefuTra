public static boolean f_gold (String num ) {
    if ( num.length() >= 3 ) {
        int d1 = Integer.parseInt(String.valueOf(num.charAt(num.length() - 1)));
        if ( d1 % 2 != 0 ) {
            return false;
        }
        int d2 = Integer.parseInt(String.valueOf(num.charAt(num.length() - 2)));
        int sum = 0;
        for ( int i = 0; i < num.length(); i++ ) {
            sum += Integer.parseInt(String.valueOf(num.charAt(i)));
        }
        return ( sum % 3 == 0 && ( d2 * 10 + d1 ) % 4 == 0 );
    } else {
        int number = Integer.parseInt(num);
        return ( number % 12 == 0 );
    }
}