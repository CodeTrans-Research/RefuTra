bool f_gold(int a1[], int a2[], int a3[], int n1, int n2, int n3, int sum) {
    unordered_set<int> s;
    for (int i = 0; i < n1; i++) {
        s.insert(a1[i]);
    }
    vector<int> al(s.begin(), s.end());
    for (int i = 0; i < n2; i++) {
        for (int j = 0; j < n3; j++) {
            if (find(al.begin(), al.end(), sum - a2[i] - a3[j]) != al.end() && find(al.begin(), al.end(), sum - a2[i] - a3[j]) != al[al.size() - 1]) {
                return true;
            }
        }
    }
    return false;
}