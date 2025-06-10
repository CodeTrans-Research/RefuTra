public static int f_gold ( int N ) {
        int B_Number = 0, cnt = 0;
        while ( N!= 0 ) {
            int rem = N % 2;
            B_Number += rem * (int) Math.pow ( 10, cnt );
            N /= 2;
            cnt++;
        }
        return B_Number;
    }