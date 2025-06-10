int f_gold ( int arr [ ], int n ) {
        vector<int> lioes(n, 1);
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j] && (arr[i] + arr[j]) % 2!= 0 && lioes[i] < lioes[j] + 1) {
                    lioes[i] = lioes[j] + 1;
                }
            }
            maxLen = max(maxLen, lioes[i]);
        }
        return maxLen;
    }