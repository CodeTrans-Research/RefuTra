int f_gold(int arr[], int n) {
        vector<int> f_gold(n, 1);
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j] && f_gold[i] < f_gold[j] + 1) {
                    f_gold[i] = f_gold[j] + 1;
                }
            }
        }
        int max = *max_element(f_gold.begin(), f_gold.end());
        return max;
    }