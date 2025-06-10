public static void f_gold(int[] arr, int n, int A, int B, int C) {
        for (int i = 0; i < n; i++) {
            arr[i] = (A * arr[i] * arr[i] + B * arr[i] + C);
        }
        int index = Integer.MIN_VALUE;
        int maximum = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            if (maximum < arr[i]) {
                index = i;
                maximum = arr[i];
            }
        }
        int i = 0, j = n - 1;
        int[] new_arr = new int[n];
        int k = 0;
        while (i < index && j > index) {
            if (arr[i] < arr[j]) {
                new_arr[k] = arr[i];
                k += 1;
                i += 1;
            } else {
                new_arr[k] = arr[j];
                k += 1;
                j -= 1;
            }
        }
        while (i < index) {
            new_arr[k] = arr[i];
            k += 1;
            i += 1;
        }
        while (j > index) {
            new_arr[k] = arr[j];
            k += 1;
            j -= 1;
        }
        for (i = 0; i < n; i++) {
            arr[i] = new_arr[i];
        }
    }