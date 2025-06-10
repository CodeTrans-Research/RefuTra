bool f_gold(string s) {
    if (s.length() >= 10) return true;
    for (int i = 1; i < s.length(); i++) {
        for (int j = i + 1; j < s.length(); j++) {
            for (int k = j + 1; k < s.length(); k++) {
                string s1 = "", s2 = "", s3 = "", s4 = "";
                try {
                    s1 = s.substr(0, i);
                    s2 = s.substr(i, j - i);
                    s3 = s.substr(j, k - j);
                    s4 = s.substr(k, s.length() - k);
                } catch (out_of_range e) {
                }
                if (s1 != s2 && s1 != s3 && s1 != s4 && s2 != s3 && s2 != s4 && s3 != s4) return true;
            }
        }
    }
    return false;
}