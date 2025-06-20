// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class SUM_SERIES_0_6_0_06_0_006_0_0006_N_TERMS{
static double f_gold ( int n ) {
  return ( 0.666 ) * ( 1 - 1 / Math . pow ( 10 , n ) ) ;
}


static double f_filled(int n) {
    return (0.666) * (1 - 1 / Math.pow(10, n));
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(1);
    param0.add(2);
    param0.add(3);
    param0.add(4);
    param0.add(5);
    param0.add(74);
    param0.add(77);
    param0.add(67);
    param0.add(9);
    param0.add(12);
    for(int i = 0; i < param0.size(); ++i)
    {
        if(Math.abs(1 - (0.0000001 + Math.abs(f_gold(param0.get(i))) )/ (Math.abs(f_filled(param0.get(i))) + 0.0000001)) < 0.001)
        {
            n_success+=1;
        }
    }
    System.out.println("#Results:" + n_success + ", " + param0.size());
}
}