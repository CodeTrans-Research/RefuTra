bool f_gold(int n) {
    bool arr[10];
    for (int i = 0; i < 10; i++) arr[i] = false;
    
    while (n > 0) {
        int digit = n % 10;
        if (arr[digit]) return false;
        arr[digit] = true;
        n = n / 10;
    }
    
    return true;
}