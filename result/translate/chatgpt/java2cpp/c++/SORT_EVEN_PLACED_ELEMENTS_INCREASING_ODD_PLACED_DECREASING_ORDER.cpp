void f_gold(int arr[], int n) {
    vector<int> evenArr;
    vector<int> oddArr;
    for (int i = 0; i < n; i++) {
        if (i % 2 != 1) {
            evenArr.push_back(arr[i]);
        } else {
            oddArr.push_back(arr[i]);
        }
    }
    sort(evenArr.begin(), evenArr.end());
    sort(oddArr.rbegin(), oddArr.rend());
    int i = 0;
    for (int j = 0; j < evenArr.size(); j++) {
        arr[i++] = evenArr[j];
    }
    for (int j = 0; j < oddArr.size(); j++) {
        arr[i++] = oddArr[j];
    }
}