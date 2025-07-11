// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class COUNT_TRAILING_ZEROES_FACTORIAL_NUMBER{
static int f_gold ( int n ) {
  int count = 0 ;
  for ( int i = 5 ;
  n / i >= 1 ;
  i *= 5 ) count += n / i ;
  return count ;
}


static int f_filled ( int n ) {
  long count = 0 ;
  int i = 5 ;
  while ( ( n / i >= 1 ) && ( n % i == 0 ) ) {
    count += ( int ) ( n / i ) ;
    i *= 5 ;
  }
  return ( int ) count ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(9);
    param0.add(43);
    param0.add(50);
    param0.add(32);
    param0.add(37);
    param0.add(51);
    param0.add(33);
    param0.add(49);
    param0.add(1);
    param0.add(75);
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