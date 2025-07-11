// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class COUNT_NUMBER_BINARY_STRINGS_WITHOUT_CONSECUTIVE_1S{
static int f_gold ( int n ) {
  int a [ ] = new int [ n ] ;
  int b [ ] = new int [ n ] ;
  a [ 0 ] = b [ 0 ] = 1 ;
  for ( int i = 1 ;
  i < n ;
  i ++ ) {
    a [ i ] = a [ i - 1 ] + b [ i - 1 ] ;
    b [ i ] = a [ i - 1 ] ;
  }
  return a [ n - 1 ] + b [ n - 1 ] ;
}


static int f_filled ( int n ) {
        int[] a = new int[n];
        int[] b = new int[n];
        a[0] = b[0] = 1;
        for ( int i = 1; i < n; i++ ) {
            a[i] = a[i - 1] + b[i - 1];
            b[i] = a[i - 1];
        }
        return a[n - 1] + b[n - 1];
    }

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(86);
    param0.add(75);
    param0.add(14);
    param0.add(5);
    param0.add(41);
    param0.add(35);
    param0.add(30);
    param0.add(89);
    param0.add(84);
    param0.add(53);
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