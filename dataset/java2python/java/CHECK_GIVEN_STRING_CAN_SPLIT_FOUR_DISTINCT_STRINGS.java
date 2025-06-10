boolean f_gold ( String s ) {
    if ( s . length ( ) >= 10 ) return true ;
    for ( int i = 1 ;
    i < s . length ( ) ;
    i ++ ) {
        for ( int j = i + 1 ;
        j < s . length ( ) ;
        j ++ ) {
            for ( int k = j + 1 ;
            k < s . length ( ) ;
            k ++ ) {
                String s1 = "" , s2 = "" , s3 = "" , s4 = "" ;
                try {
                s1 = s . substring ( 0 , i ) ;
                s2 = s . substring ( i , j ) ;
                s3 = s . substring ( j , k ) ;
                s4 = s . substring ( k , s . length ( ) ) ;
                }
                catch ( StringIndexOutOfBoundsException e ) {
                }
                if ( !s1.equals(s2) && !s1.equals(s3) && !s1.equals(s4) && !s2.equals(s3) && !s2.equals(s4) && !s3.equals(s4) ) return true ;
            }
        }
    }
    return false ;
}