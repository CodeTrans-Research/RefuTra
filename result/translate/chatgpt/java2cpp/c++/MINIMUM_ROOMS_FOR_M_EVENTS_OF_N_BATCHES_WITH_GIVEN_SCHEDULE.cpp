int f_gold(string slots[], int n, int m) {
    int* counts = new int[m];
    for (int i = 0; i < m; i++) counts[i] = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i < n && j < slots[i].length()) {
                if (slots[i][j] == '1') counts[j]++;
            }
        }
    }
    int max = -1;
    for (int i = 0; i < m; i++) {
        if (max < counts[i]) max = counts[i];
    }
    return max;
}