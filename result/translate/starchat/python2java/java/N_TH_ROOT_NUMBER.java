public static double f_gold ( int A, int N ) {
        Random rand = new Random();
        double xPre = rand.nextDouble() * 100;
        double eps = 0.001;
        double delX = Double.MAX_VALUE;
        double xK = 0.0;
        while ( delX > eps ) {
            xK = ( ( N - 1.0 ) * xPre + A / Math.pow( xPre, N - 1 ) ) / N;
            delX = Math.abs( xK - xPre );
            xPre = xK;
        }
        return xK;
    }