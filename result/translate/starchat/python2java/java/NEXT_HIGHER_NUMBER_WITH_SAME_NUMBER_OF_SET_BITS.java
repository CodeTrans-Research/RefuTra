public static int f_gold ( int x ) {
        int next = 0;
        if ( x!= 0 ) {
            int rightOne = x & -x;
            int nextHigherOneBit = x + rightOne;
            int rightOnesPattern = x ^ nextHigherOneBit;
            rightOnesPattern = rightOnesPattern / rightOne;
            rightOnesPattern = rightOnesPattern >> 2;
            next = nextHigherOneBit | rightOnesPattern;
        }
        return next;
    }