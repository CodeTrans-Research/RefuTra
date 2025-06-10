public boolean f_gold(int[] a, int[] b, int n, int k) {
    // slicing the arrays a and b to only include the first n elements
    Arrays.copyOfRange(a, 0, n);
    Arrays.copyOfRange(b, 0, n);
    
    Arrays.sort(a);
    Arrays.sort(b);
    
    for (int i = 0; i < n; i++) {
        if (a[i] + b[i] < k) {
            return false;
        }
    }
    return true;
}