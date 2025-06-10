bool f_gold ( int p ) {
    long checkNumber = pow ( 2, p ) - 1;
    long nextval = 4 % checkNumber;
    for ( int i = 1; i < p - 1; i++ ) nextval = ( nextval * nextval - 2 ) % checkNumber;
    return ( nextval == 0 );
}