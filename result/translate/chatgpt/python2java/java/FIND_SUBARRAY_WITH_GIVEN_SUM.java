public int f_gold(int[] arr, int n, int sum) {
    for (int i = 0; i < n; i++) {
        int curr_sum = arr[i];
        int j = i + 1;
        while (j <= n) {
            if (curr_sum == sum) {
                System.out.println("Sum found between");
                System.out.println("indexes " + i + " and " + (j - 1));
                return 1;
            }
            if (curr_sum > sum || j == n) {
                break;
            }
            curr_sum = curr_sum + arr[j];
            j++;
        }
    }
    System.out.println("No subarray found");
    return 0;
}