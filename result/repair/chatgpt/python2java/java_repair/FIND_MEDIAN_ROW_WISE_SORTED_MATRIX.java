 int f_gold(int m[][], int r, int c) {
    int mi = Integer.MAX_VALUE;
    int mx = Integer.MIN_VALUE;
    for (int i = 0; i < r; i++) {
        if (m[i][0] < mi) {
            mi = m[i][0];
        }
        if (m[i][c - 1] > mx) {
            mx = m[i][c - 1];
        }
    }
    int desired = (r * c + 1) / 2;
    while (mi < mx) {
        int mid = mi + (mx - mi) / 2;
        int[] place = {0};
        for (int i = 0; i < r; i++) {
            int j = upper_bound(m[i], mid);
            place[0] = place[0] + j;
        }
        if (place[0] < desired) {
            mi = mid + 1;
        } else {
            mx = mid;
        }
    }
    System.out.println("Median is " + mi);
    return mi;
}
