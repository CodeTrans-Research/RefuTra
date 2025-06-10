public static int f_gold ( int n ) {
        int x = 0, res = 0, yCount = 0;
        while ( yCount * yCount < n ) yCount++;
        while ( yCount > 0 ) {
            res += yCount;
            x++;
            while ( yCount > 0 && ( x * x + ( yCount - 1 ) * ( yCount - 1 ) >= n ) ) yCount--;
        }
        return res;
    }