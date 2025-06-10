  int f_gold ( int n [ ] ) {
        int res = 0;
        for (int j=n.length-1;j>-1;j--){
            res += n [ j ];
        }
        return res;
    }
