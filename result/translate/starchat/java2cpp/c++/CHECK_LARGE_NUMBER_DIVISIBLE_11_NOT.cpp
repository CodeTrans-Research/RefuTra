bool f_gold ( string str ) {
        int n = str. length ( );
        int oddDigSum = 0, evenDigSum = 0;
        for ( int i = 0; i < n; i++ ) {
            if ( i % 2 == 0 ) oddDigSum += ( str[i] - '0' );
            else evenDigSum += ( str[i] - '0' );
        }
        return ( ( oddDigSum - evenDigSum ) % 11 == 0 );
    }