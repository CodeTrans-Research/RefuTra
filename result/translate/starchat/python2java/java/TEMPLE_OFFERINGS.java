public static int f_gold ( int n, int[] templeHeight ) {
        int sum = 0;
        for ( int i = 0; i < n; i++ ) {
            int left = 0, right = 0;
            for ( int j = i - 1; j >= 0 && templeHeight[j] < templeHeight[j + 1]; j-- ) {
                left++;
            }
            for ( int j = i + 1; j < n && templeHeight[j] < templeHeight[j - 1]; j++ ) {
                right++;
            }
            sum += Math.max(right, left) + 1;
        }
        return sum;
    }