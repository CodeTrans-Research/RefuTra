string f_gold ( string s, char c1, char c2 ) {
        int l = s.length();
        vector<char> arr(s.begin(), s.end());
        for ( int i = 0; i < l; i++ ) {
            if ( arr[i] == c1 ) arr[i] = c2;
            else if ( arr[i] == c2 ) arr[i] = c1;
        }
        return string(arr.begin(), arr.end());
    }