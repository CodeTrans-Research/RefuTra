double f_gold(int n){
        if ( n < 0 ) return 0;
        if ( n <= 1 ) return 1;
        double digits = 0;
        for ( double i = 2 ; i <= n ; i++ ) digits +=  ( Math.log10 ( i ) + 0.5 );
        return digits + 1;
    }
