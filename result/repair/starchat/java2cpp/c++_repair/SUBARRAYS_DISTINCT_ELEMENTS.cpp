int f_gold(vector<int> arr, int n) {
int[] s;
    int j = 0;
    int ans = 0;
    for (int i = 0; i < n; i++) {
        while (j < n &&!s.count(arr[j])) {
            s.insert(arr[j]);
            j++;
        }
        ans += ((j - i) * (j - i + 1)) / 2;
        s.erase(arr[i]);
    }
    return ans;
}
