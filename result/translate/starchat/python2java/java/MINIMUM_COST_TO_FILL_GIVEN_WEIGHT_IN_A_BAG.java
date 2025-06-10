public static int f_gold ( int[] cost, int n, int W ) {
        int[][] min_cost = new int[n + 1][W + 1];
        for ( int i = 0; i <= W; i++ ) {
            min_cost[0][i] = Integer.MAX_VALUE;
        }
        for ( int i = 1; i <= n; i++ ) {
            for ( int j = 1; j <= W; j++ ) {
                if ( cost[i - 1]!= -1 && j >= cost[i - 1] ) {
                    min_cost[i][j] = Math.min(min_cost[i][j], min_cost[i - 1][j - cost[i - 1]] + cost[i - 1]);
                } else {
                    min_cost[i][j] = Math.min(min_cost[i][j], min_cost[i - 1][j]);
                }
            }
        }
        if (min_cost[n][W] == Integer.MAX_VALUE) {
            return -1;
        } else {
            return min_cost[n][W];
        }
    }