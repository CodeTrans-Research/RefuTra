// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class FIND_WHETHER_GIVEN_INTEGER_POWER_3_NOT{
static boolean f_gold ( int n ) {
  return 1162261467 % n == 0 ;
}


static boolean f_filled ( int n ) {
  return 1162261467 % n == 0 ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(1);
    param0.add(3);
    param0.add(27);
    param0.add(9);
    param0.add(-9);
    param0.add(11);
    param0.add(57);
    param0.add(21);
    param0.add(60);
    param0.add(44);
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