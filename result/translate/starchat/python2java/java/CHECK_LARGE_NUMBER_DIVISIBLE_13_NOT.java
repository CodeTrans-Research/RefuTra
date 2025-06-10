public static boolean f_gold ( String num ) {
        int length = num. length ();
        if ( length == 1 && num. charAt ( 0 ) == '0' ) {
            return true;
        }
        if ( length % 3 == 1 ) {
            num = num + "00";
            length += 2;
        }
        if ( length % 3 == 2 ) {
            num = num + "0";
            length += 1;
        }
        int sum = 0;
        int p = 1;
        for ( int i = length - 1; i >= 0; i -= 3 ) {
            int group = 0;
            group += num. charAt ( i ) - '0';
            i--;
            group += ( num. charAt ( i ) - '0' ) * 10;
            i--;
            group += ( num. charAt ( i ) - '0' ) * 100;
            sum += group * p;
            p *= -1;
        }
        sum = Math. abs ( sum );
        return ( sum % 13 == 0 );
    }