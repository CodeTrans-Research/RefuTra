bool f_gold (vector<int> a, vector<int> b, int n, int k) {
        sort(a.rbegin(), a.rend());
        sort(b.begin(), b.end());
        for (int i = 0; i < n; i++)
            if (a[i] + b[i] < k)
                return false;
        return true;
    }