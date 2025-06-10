public static int f_gold(int[] arr, int l, int r, int x) {
    if (r >= l) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == x) {
            return mid;
        } else if (arr[mid] > x) {
            return f_gold(arr, l, mid - 1, x);
        } else {
            return f_gold(arr, mid + 1, r, x);
        }
    } else {
        return -1;
    }
}