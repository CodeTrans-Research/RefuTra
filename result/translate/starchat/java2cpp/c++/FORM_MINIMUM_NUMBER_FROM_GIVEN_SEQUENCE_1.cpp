string f_gold ( string seq ) {
        int n = seq.length();
        if (n >= 9) return "-1";
        char result[n + 1];
        int count = 1;
        for (int i = 0; i <= n; i++) {
            if (i == n || seq[i] == 'I') {
                for (int j = i - 1; j >= 0; j--) {
                    result[j + 1] = (char)('0' + count++);
                    if (j >= 0 && seq[j] == 'I') break;
                }
            }
        }
        return string(result);
    }