bool f_gold ( string s ) {
        int l = s.length();
        if (l % 2 == 1) return false;
        int i = 0, j = l - 1;
        while (i < j) {
            if (s[i]!= 'a' || s[j]!= 'b') return false;
            i++, j--;
        }
        return true;
    }