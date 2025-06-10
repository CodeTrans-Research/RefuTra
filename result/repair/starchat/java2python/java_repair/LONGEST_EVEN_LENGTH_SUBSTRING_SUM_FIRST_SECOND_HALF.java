  int f_gold ( String str ) {
        int n = str. length ();
        int maxlen = 0;
        for ( int i = 0; i < n; i++ ) {
            for (int j=i+1;j<n;j=j+2){
                int length = j - i;
                int leftsum = 0;
                int rightsum = 0;
                for ( int k = 0; k < length / 2; k++ ) {
                    leftsum += ( str. charAt ( i + k ) - '0' );
                    rightsum += ( str. charAt ( i + k + length / 2 ) - '0' );
                }
                if ( leftsum == rightsum && maxlen < length ) {
                    maxlen = length;
                }
            }
        }
        return maxlen;
    }
