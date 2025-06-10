public static int f_gold ( int l ) {
        int leafNodeCount = (int) Math.pow ( 2, l - 1 );
        int sumLastLevel = 0;
        sumLastLevel = ( leafNodeCount * ( leafNodeCount + 1 ) ) / 2;
        int sum = sumLastLevel * l;
        return sum;
    }