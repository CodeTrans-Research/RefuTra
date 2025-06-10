std::string f_gold(std::string str, int k) {
    std::string ans = "";
    std::vector<char> palin(str.begin(), str.end());
    int l = 0;
    int r = str.length() - 1;
    while (l < r) {
        if (str[l] != str[r]) {
            palin[l] = palin[r] = std::max(str[l], str[r]);
            k--;
        }
        l++;
        r--;
    }
    if (k < 0) {
        return "Not possible";
    }
    l = 0;
    r = str.length() - 1;
    while (l <= r) {
        if (l == r) {
            if (k > 0) {
                palin[l] = '9';
            }
        }
        if (palin[l] < '9') {
            if (k >= 2 && palin[l] == str[l] && palin[r] == str[r]) {
                k -= 2;
                palin[l] = palin[r] = '9';
            } else if (k >= 1 && (palin[l] != str[l] || palin[r] != str[r])) {
                k--;
                palin[l] = palin[r] = '9';
            }
        }
        l++;
        r--;
    }
    for (int i = 0; i < palin.size(); i++) {
        ans += palin[i];
    }
    return ans;
}