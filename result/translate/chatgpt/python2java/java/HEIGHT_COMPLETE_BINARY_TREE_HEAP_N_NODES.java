public int f_gold(int N) {
    return (int) Math.ceil(Math.log(N + 1) / Math.log(2)) - 1;
}