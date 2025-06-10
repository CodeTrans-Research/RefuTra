int f_gold(int a[], int n) {
    int *copy = new int[n];
    std::copy(a, a + n, copy);
    std::sort(copy, copy + n);
    int sum = 0;
    bool flag = false;
    int len = 0;
    for (int i = 0; i < n - 1; i++) {
        if ((copy[i] == copy[i + 1] || copy[i] - copy[i + 1] == 1) && !flag) {
            flag = true;
            len = copy[i + 1];
            i++;
        } else if ((copy[i] == copy[i + 1] || copy[i] - copy[i + 1] == 1) && (flag)) {
            sum = sum + copy[i + 1] * len;
            flag = false;
            i++;
        }
    }
    delete[] copy;
    return sum;
}