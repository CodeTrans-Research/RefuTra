// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class SUM_BINOMIAL_COEFFICIENTS_1{
static int f_gold ( int n ) {
  return ( 1 << n ) ;
}


static int f_filled(int n) {
    return (1 << n);
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(1);
    param0.add(2);
    param0.add(3);
    param0.add(4);
    param0.add(5);
    param0.add(6);
    param0.add(7);
    param0.add(8);
    param0.add(9);
    param0.add(10);
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
