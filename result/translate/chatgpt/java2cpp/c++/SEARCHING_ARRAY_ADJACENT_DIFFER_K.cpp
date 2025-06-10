int f_gold(int arr[], int n, int x, int k) {
    int i = 0;
    while (i < n) {
        if (arr[i] == x)
            return i;
        i = i + std::max(1, std::abs(arr[i] - x) / k);
    }
    std::cout << "number is not present!" << std::endl;
    return -1;
}