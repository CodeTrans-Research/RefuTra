public static int f_gold ( int x, int y, int z ) {
        if (! (y/x) % 1) return y;
        if (! (y/z) % 1) return z;
        return x;
    }