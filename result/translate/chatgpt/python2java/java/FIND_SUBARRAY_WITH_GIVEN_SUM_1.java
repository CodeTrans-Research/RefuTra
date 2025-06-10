public static int f_gold(int arr[], int n, int sum) {
    int curr_sum = arr[0];
    int start = 0;
    int i = 1;
    while (i <= n) {
        while (curr_sum > sum && start < i - 1) {
            curr_sum = curr_sum - arr[start];
            start++;
        }
        if (curr_sum == sum) {
            System.out.println("Sum found between indexes");
            System.out.println(start + " and " + (i - 1));
            return 1;
        }
        if (i < n) {
            curr_sum = curr_sum + arr[i];
        }
        i++;
    }
    System.out.println("No subarray found");
    return 0;
}