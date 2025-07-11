// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT{
static boolean f_gold ( int n ) {
  if ( n == 0 ) return false ;
  while ( n != 1 ) {
    if ( n % 4 != 0 ) return false ;
    n = n / 4 ;
  }
  return true ;
}


static boolean f_filled ( int n ) {
        if ( n == 0 ) {
            return false;
        }
        while ( n!= 1 ) {
            if ( n % 4!= 0 ) {
                return false;
            }
            n = n / 4;
        }
        return true;
    }

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(1);
    param0.add(16);
    param0.add(15);
    param0.add(91);
    param0.add(82);
    param0.add(18);
    param0.add(31);
    param0.add(6);
    param0.add(93);
    param0.add(35);
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