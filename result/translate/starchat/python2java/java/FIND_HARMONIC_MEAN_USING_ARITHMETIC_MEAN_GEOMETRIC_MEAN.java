public static double f_gold ( double a, double b ) {
        double AM = ( a + b ) / 2;
        double GM = Math.sqrt ( a * b );
        double HM = ( GM * GM ) / AM;
        return HM;
    }