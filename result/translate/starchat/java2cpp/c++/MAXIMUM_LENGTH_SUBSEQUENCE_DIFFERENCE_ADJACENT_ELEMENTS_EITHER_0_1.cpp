int f_gold ( int arr [ ], int n ) {
        vector<int> mls(n,1);
        for (int i = 1; i < n; i++)
            for (int j = 0; j < i; j++)
                if (abs(arr[i] - arr[j]) <= 1 && mls[i] < mls[j] + 1)
                    mls[i] = mls[j] + 1;
        int max = *max_element(mls.begin(), mls.end());
        return max;
    }