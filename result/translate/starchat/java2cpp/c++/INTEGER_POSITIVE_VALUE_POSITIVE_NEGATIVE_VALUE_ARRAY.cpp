int f_gold ( int arr [ ], int n ) {
    unordered_map<int, int> hash;
    int maximum = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] < 0) hash[abs(arr[i])]--;
        else hash[abs(arr[i])]++;
        if (hash[abs(arr[i])] > maximum) maximum = hash[abs(arr[i])];
    }
    for (int i = 0; i < n; i++) if (hash[arr[i]] > 0) return arr[i];
    return -1;
}