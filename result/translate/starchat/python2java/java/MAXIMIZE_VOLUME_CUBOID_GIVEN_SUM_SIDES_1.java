public static int f_gold ( int s ) {
        int length = ( s / 3 );
        s -= length * 3;
        int breadth = s / 2;
        int height = s - breadth;
        return ( length * breadth * height );
    }