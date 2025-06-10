public static String f_gold ( String str, int k ) {
        char [] palin = str.toCharArray();
        int l = 0, r = palin.length - 1;
        while ( l <= r ) {
            if ( palin [ l ]!= palin [ r ] ) {
                palin [ l ] = palin [ r ] = Math.max ( palin [ l ], palin [ r ] );
                k--;
            }
            l++;
            r--;
        }
        if ( k < 0 ) return "Not possible";
        l = 0, r = palin.length - 1;
        while ( l <= r ) {
            if ( l == r ) {
                if ( k > 0 ) palin [ l ] = '9';
            }
            if ( palin [ l ] < '9' ) {
                if ( k >= 2 && palin [ l ] == str.charAt ( l ) && palin [ r ] == str.charAt ( r ) ) {
                    k--;
                    palin [ l ] = palin [ r ] = '9';
                }
                else if ( k >= 1 && ( palin [ l ]!= str.charAt ( l ) || palin [ r ]!= str.charAt ( r ) ) ) {
                    k--;
                    palin [ l ] = palin [ r ] = '9';
                }
            }
            l++;
            r--;
        }
        return new String ( palin );
    }