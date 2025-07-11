// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class MAXIMUM_SUM_IARRI_AMONG_ROTATIONS_GIVEN_ARRAY_1{
static int f_gold ( int arr [ ] , int n ) {
  int cum_sum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) cum_sum += arr [ i ] ;
  int curr_val = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) curr_val += i * arr [ i ] ;
  int res = curr_val ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    int next_val = curr_val - ( cum_sum - arr [ i - 1 ] ) + arr [ i - 1 ] * ( n - 1 ) ;
    curr_val = next_val ;
    res = Math . max ( res , next_val ) ;
  }
  return res ;
}


static int f_filled(int[] arr, int n) {
    int cum_sum = 0;
    for (int i = 0; i < n; i++) {
        cum_sum += arr[i];
    }
    int curr_val = 0;
    for (int i = 0; i < n; i++) {
        curr_val += i * arr[i];
    }
    int res = curr_val;
    for (int i = 1; i < n; i++) {
        int next_val = (curr_val - (cum_sum - arr[i - 1]) + arr[i - 1] * (n - 1));
        curr_val = next_val;
        res = Math.max(res, next_val);
    }
    return res;
}

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{6,6,13,14,16,20,24,24,24,27,28,36,49,51,55,56,62,69,74,74,76,85,86,90,92,98});
    param0.add(new int[]{-42,96,68,64,14,-74,76,42,34,-92,-20,28,-80,-34,-22,96,-46,96,10,-82,82,50,-24,48,56,72,-40,-86,84,66,-62,50,-76,34});
    param0.add(new int[]{0,0,0,0,0,1,1,1,1,1,1});
    param0.add(new int[]{37,88,70,86,24,62,34,44,37,42,46,34,23,32,55,2,5,70,30,46,40,65,91,4,7,74,46,12,30,22,1,91,89,88,97,6,6,11,33,14,68,24});
    param0.add(new int[]{-92,-90,-70,-70,-10,2,10,12,14,40,44,46,64,68,68,96});
    param0.add(new int[]{1,0,1,0,0,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1});
    param0.add(new int[]{9,15,15,17,19,20,21,23,25,25,25,32,32,33,45,51,54,59,68,71,71,71,72,75,78,80,82,82,88,89,92,93,94,97});
    param0.add(new int[]{52,-78,-80,32,-56,-98,-36,86,34,-36,42,46,50,0,34,-46,-2,-18,-96,12,-42,62,32,78,66,-8,50,60,10,-18,66,80,-24,-98,8,48,34,44,-80,-34,72,0,-60,52,40,20});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{45,35,25,7,24,73,25,86,48,70,47,91,96,15,39,9});
    List<Integer> param1 = new ArrayList<>();
    param1.add(13);
    param1.add(27);
    param1.add(10);
    param1.add(39);
    param1.add(11);
    param1.add(15);
    param1.add(22);
    param1.add(45);
    param1.add(33);
    param1.add(8);
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i),param1.get(i)) == f_gold(param0.get(i),param1.get(i)))
        {
            n_success+=1;
        }
    }
    System.out.println("#Results:" + n_success + ", " + param0.size());
}
}