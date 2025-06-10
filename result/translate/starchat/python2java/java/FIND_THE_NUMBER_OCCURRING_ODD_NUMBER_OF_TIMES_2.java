public static int f_gold ( int[] ar, int ar_size ) {
        int res = 0;
        for ( int i = 0; i < ar_size; i++ ) {
            res = res ^ ar[i];
        }
        return res;
    }

Explanation:
The logic is same as in python. We iterate over the array and xor all the elements together to get the final result.