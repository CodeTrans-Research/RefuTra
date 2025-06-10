bool f_gold (vector<int> a, int n) {
        int count_odd = 0, count_even = 0;
        for (int i = 0; i < n; i++) {
            if ((a[i] & 1) == 1) count_odd++;
            else count_even++;
        }
        return (count_odd % 2 == 1 && count_even % 2 == 1);
    }