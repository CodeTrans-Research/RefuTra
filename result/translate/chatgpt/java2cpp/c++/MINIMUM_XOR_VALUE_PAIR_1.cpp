int f_gold(int arr[], int n) {
    int* newArr = new int[n];
    for(int i=0; i<n; i++){
        newArr[i] = arr[i];
    }
    std::sort(newArr, newArr+n);
    int minXor = std::numeric_limits<int>::max();
    int val = 0;
    for(int i=0; i<n-1; i++){
        val = newArr[i] ^ newArr[i+1];
        minXor = std::min(minXor, val);
    }
    delete[] newArr;
    return minXor;
}