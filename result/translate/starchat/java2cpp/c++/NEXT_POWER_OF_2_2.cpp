int f_gold ( int n ) {
    int i = 0;
    while (n!= 0) {
        n = n & (n-1);
        i++;
    }
    return i;
}