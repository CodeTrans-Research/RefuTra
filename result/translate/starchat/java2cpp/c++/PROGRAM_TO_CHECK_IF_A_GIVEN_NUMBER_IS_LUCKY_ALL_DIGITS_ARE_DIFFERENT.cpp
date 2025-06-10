bool f_gold ( int n ) {
    vector <bool> arr(10, false);
    while (n > 0) {
        int digit = n % 10;
        if (arr[digit]) return false;
        arr[digit] = true;
        n /= 10;
    }
    return true;
}