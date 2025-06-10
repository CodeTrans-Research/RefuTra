bool f_gold(int a[], int b[], int n, int k) {
    int *a_copy = new int[n];
    int *b_copy = new int[n];
    
    std::copy(a, a + n, a_copy);
    std::copy(b, b + n, b_copy);
    
    std::sort(a_copy, a_copy + n, std::greater<int>());
    std::sort(b_copy, b_copy + n);
    
    for(int i = 0; i < n; i++) {
        if(a_copy[i] + b_copy[i] < k) {
            delete[] a_copy;
            delete[] b_copy;
            return false;
        }
    }
    
    delete[] a_copy;
    delete[] b_copy;
    return true;
}