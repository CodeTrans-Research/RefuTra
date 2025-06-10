public static int f_gold(int n) {
    int x = 0;
    int res = 0;
    int yCount = 0;
    while (yCount * yCount < n) {
        yCount = yCount + 1;
    }
    while (yCount != 0) {
        res = res + yCount;
        x = x + 1;
        while (yCount != 0 && (x * x + (yCount - 1) * (yCount - 1) >= n)) {
            yCount = yCount - 1;
        }
    }
    return res;
}