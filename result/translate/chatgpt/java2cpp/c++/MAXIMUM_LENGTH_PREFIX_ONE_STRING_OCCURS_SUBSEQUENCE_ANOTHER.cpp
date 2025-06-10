int f_gold(string s, string t) {
    int count = 0;
    for (int i = 0; i < t.length(); i++) {
        if (count == t.length()) break;
        if (t[i] == s[count]) count++;
    }
    return count;
}