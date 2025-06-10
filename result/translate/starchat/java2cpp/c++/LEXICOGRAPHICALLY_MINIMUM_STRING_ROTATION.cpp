string f_gold ( string str ) {
        int n = str.length();
        vector<string> arr(n);
        string concat = str + str;
        for (int i = 0; i < n; i++) {
            arr[i] = concat.substr(i, n);
        }
        sort(arr.begin(), arr.end());
        return arr[0];
    }