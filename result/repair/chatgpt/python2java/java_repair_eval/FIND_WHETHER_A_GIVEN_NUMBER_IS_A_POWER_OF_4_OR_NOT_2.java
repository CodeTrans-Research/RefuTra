// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT_2{
static boolean f_gold ( int n ) {
  return n != 0 && ( ( n & ( n - 1 ) ) == 0 ) && ( n & 0xAAAAAAAA ) == 0 ;
}


static boolean f_filled(int n) {
    return (!((n&0xAAAAAAAA)!=0) && ((n&(n-1))==0 && n!=0));
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(1);
    param0.add(4);
    param0.add(64);
    param0.add(-64);
    param0.add(128);
    param0.add(1024);
    param0.add(97);
    param0.add(86);
    param0.add(14);
    param0.add(99);
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