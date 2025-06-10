bool f_gold (vector<int> arr, int N) {
        arr = vector<int>(arr.begin(), arr.begin() + N);
        sort(arr.begin(), arr.end());
        for (int i = 0; i < N - 2; i++)
            if (arr[i] + arr[i + 1] > arr[i + 2])
                return true;
        return false;
    }