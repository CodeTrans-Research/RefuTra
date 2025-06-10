bool f_gold(int arr[], int N) {
    int* newArr = new int[N];
    for (int i = 0; i < N; i++) {
        newArr[i] = arr[i];
    }
    
    if (N < 3) {
        delete[] newArr;
        return false;
    }
    
    sort(newArr, newArr + N);
    
    for (int i = 0; i < N - 2; i++) {
        if (newArr[i] + newArr[i + 1] > newArr[i + 2]) {
            delete[] newArr;
            return true;
        }
    }
    
    delete[] newArr;
    return false;
}