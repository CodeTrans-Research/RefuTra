bool is_sorted(int arr[], int n) {
        if (n <= 1) return true;
        for (int i = 1; i < n; i++) {
            if (arr[i - 1] > arr[i]) return false;
        }
        return true;
    }