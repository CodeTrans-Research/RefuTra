int f_gold ( int ar [ ], int n ) {
        int res = 0 ;
        sort(ar, ar+n);
        for (int i = 0; i < n; i++) {
            int count = 1;
            for (int j = i+1; j < n; j++) {
                if (ar[i] == ar[j]) count++;
                else break;
            }
            res = max(res, count);
        }
        return res;
    }