public static int f_gold ( int n ) {
        int l = (int) Math.sqrt ( n );
        int sq = l * l;
        if ( sq == n ) return l * 4;
        int row = n / l;
        int perimeter = 2 * ( l + row );
        if ( n % l!= 0 ) perimeter += 2;
        return perimeter;
    }