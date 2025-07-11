// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class ADD_1_TO_A_GIVEN_NUMBER_1{
static int f_gold ( int x ) {
  return ( - ( ~ x ) ) ;
}


static int f_filled ( int x ) {
        return ( - ( ~ x ) );
    }

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(20);
    param0.add(68);
    param0.add(52);
    param0.add(61);
    param0.add(3);
    param0.add(88);
    param0.add(41);
    param0.add(78);
    param0.add(94);
    param0.add(18);
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