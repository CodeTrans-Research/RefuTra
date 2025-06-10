public static int f_gold(int[] a, int n) {
    if (n == 1)
      return a[0];

    int max_neg = -999999999;
    int count_neg = 0;
    int count_zero = 0;
    int prod = 1;

    for (int i = 0; i < n; i++) {
      if (a[i] == 0) {
        count_zero += 1;
        continue;
      }
      if (a[i] < 0) {
        count_neg += 1;
        max_neg = Math.max(max_neg, a[i]);
      }
      prod = prod + a[i];
    }

    if (count_zero == n)
      return 0;

    if (count_neg % 2 != 0) {
      if ((count_neg == 1) && (count_zero > 0) && (count_zero + count_neg == n))
        return 0;
      prod = prod / max_neg;
    }

    return prod;
}