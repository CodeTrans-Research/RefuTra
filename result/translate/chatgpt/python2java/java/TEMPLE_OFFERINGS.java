int f_gold(int n, int[] templeHeight) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        int left = 0;
        int right = 0;
        for (int j = i - 1; j >= 0; j--) {
            if (templeHeight[j] < templeHeight[j + 1]) {
                left += 1;
            } else {
                break;
            }
        }
        for (int j = i + 1; j < n; j++) {
            if (templeHeight[j] < templeHeight[j - 1]) {
                right += 1;
            } else {
                break;
            }
        }
        sum += Math.max(right, left) + 1;
    }
    return sum;
}