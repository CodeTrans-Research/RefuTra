public static int f_gold ( String s, int n ) {
        String s1 = s;
        for ( int i = 1; i < n; i++ ) {
            s += s1;
        }
        return Integer.parseInt(s);
    }