int f_gold ( int [ ] A, int [ ] B, int n ) {
    unordered_map<int, int> hash;
    for (int i = 0; i < n; i++) {
        if (hash.find(A[i])!= hash.end()) hash[A[i]]++;
        else hash[A[i]] = 1;
        if (hash.find(B[i])!= hash.end()) hash[B[i]]++;
        else hash[B[i]] = 1;
    }
    int sum = 0;
    for (auto it : hash) {
        if (it.second == 1) sum += it.first;
    }
    return sum;
}