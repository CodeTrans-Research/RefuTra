public static int f_gold(int arr1[], int arr2[], int m, int n, int k) {
    int sorted1[] = new int[m + n];
    int i = 0;
    int j = 0;
    int d = 0;
    while (i < m && j < n) {
        if (arr1[i] < arr2[j]) {
            sorted1[d] = arr1[i];
            i += 1;
        } else {
            sorted1[d] = arr2[j];
            j += 1;
        }
        d += 1;
    }
    while (i < m) {
        sorted1[d] = arr1[i];
        d += 1;
        i += 1;
    }
    while (j < n) {
        sorted1[d] = arr2[j];
        d += 1;
        j += 1;
    }
    return sorted1[k - 1];
}