bool f_gold ( int A [ ], int arr_size, int sum ) {
    for (int i = 0; i < arr_size - 2; i++) {
        for (int j = i + 1; j < arr_size - 1; j++) {
            for (int k = j + 1; k < arr_size; k++) {
                if (A[i] + A[j] + A[k] == sum) {
                    cout << "Triplet is " << A[i] << ", " << A[j] << ", " << A[k] << endl;
                    return true;
                }
            }
        }
    }
    return false;
}