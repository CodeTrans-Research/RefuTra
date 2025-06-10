public static int f_gold(int arr[], int low, int high) {
    if (high >= low) {
        int mid = low + (high - low) / 2;
        if ((mid == high || arr[mid + 1] == 0) && (arr[mid] == 1)) {
            return mid + 1;
        }
        if (arr[mid] == 1) {
            return f_gold(arr, mid + 1, high);
        }
        return f_gold(arr, low, mid - 1);
    }
    return 0;
}