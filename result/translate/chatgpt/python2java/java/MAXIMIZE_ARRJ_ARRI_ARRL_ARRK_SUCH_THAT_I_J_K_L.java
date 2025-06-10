public static int f_gold(int[] arr, int n) {
    if (n < 4) {
        System.out.println("The array should have atleast 4 elements");
        return Integer.MIN_VALUE;
    }
    int[] table1 = new int[n + 1];
    int[] table2 = new int[n];
    int[] table3 = new int[n - 1];
    int[] table4 = new int[n - 2];
    for (int i = n - 1; i >= 0; i--) {
        table1[i] = Math.max((i + 1 < n ? table1[i + 1] : Integer.MIN_VALUE), arr[i]);
    }
    for (int i = n - 2; i >= 0; i--) {
        table2[i] = Math.max((i + 1 < n ? table2[i + 1] : Integer.MIN_VALUE), table1[i + 1] - arr[i]);
    }
    for (int i = n - 3; i >= 0; i--) {
        table3[i] = Math.max((i + 1 < n - 1 ? table3[i + 1] : Integer.MIN_VALUE), table2[i + 1] + arr[i]);
    }
    for (int i = n - 4; i >= 0; i--) {
        table4[i] = Math.max((i + 1 < n - 2 ? table4[i + 1] : Integer.MIN_VALUE), table3[i + 1] - arr[i]);
    }
    return table4[0];
}