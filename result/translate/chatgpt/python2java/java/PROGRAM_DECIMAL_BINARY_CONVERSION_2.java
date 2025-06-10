public static int f_gold(int N) {
    int B_Number = 0;
    int cnt = 0;
    while (N != 0) {
        int rem = N % 2;
        int c = (int) Math.pow(10, cnt);
        B_Number += rem * c;
        N /= 2;
        cnt += 1;
    }
    return B_Number;
}