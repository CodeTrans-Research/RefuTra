// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class COUNTING_PAIRS_PERSON_CAN_FORM_PAIR_ONE_1{
static int f_gold ( int x ) {
  int dp [ ] = new int [ x + 1 ] ;
  dp [ 0 ] = dp [ 1 ] = 1 ;
  for ( int i = 2 ;
  i <= x ;
  i ++ ) dp [ i ] = dp [ i - 1 ] + ( i - 1 ) * dp [ i - 2 ] ;
  return dp [ x ] ;
}


static int f_filled ( int x ) {
        int[] dp = new int[x + 1];
        dp[0] = dp[1] = 1;
        for ( int i = 2; i <= x; i++ ) {
            dp[i] = dp[i - 1] + (i - 1) * dp[i - 2];
        }
        return dp[x];
    }

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(22);
    param0.add(92);
    param0.add(15);
    param0.add(81);
    param0.add(3);
    param0.add(30);
    param0.add(88);
    param0.add(4);
    param0.add(43);
    param0.add(92);
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i)) == f_gold(param0.get(i)))
        {
            n_success+=1;
        }
    }
    System.out.println("#Results:" + n_success + ", " + param0.size());
}
}