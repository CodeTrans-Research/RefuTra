public static double f_gold(double A, double N) {
    Random random = new Random();
    random.setSeed(1);
    double xPre = random.nextFloat() * 10;
    double eps = 0.001;
    double delX = 2147483647;
    double xK = 0.0;
    
    while (delX > eps) {
        xK = ((N - 1.0) * xPre + A / Math.pow(xPre, N - 1)) / N;
        delX = Math.abs(xK - xPre);
        xPre = xK;
    }
    
    return xK;
}