int f_gold(int arr1[], int arr2[], int m, int n, int x) {
    int count = 0;
    unordered_set<int> us;
    for (int i = 0; i < m; i++) 
        us.insert(arr1[i]);
    for (int j = 0; j < n; j++) 
        if (us.find(x - arr2[j]) != us.end()) 
            count++;
    return count;
}