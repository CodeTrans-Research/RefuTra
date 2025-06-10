int f_gold ( int n, int p ) {
    int ans = 0;
    for ( int i = 1; i <= n; i++ ) {
        int count = 0, temp = i;
        while ( temp % p == 0 ) {
            count++;
            temp /= p;
        }
        ans += count;
    }
    return ans;
}