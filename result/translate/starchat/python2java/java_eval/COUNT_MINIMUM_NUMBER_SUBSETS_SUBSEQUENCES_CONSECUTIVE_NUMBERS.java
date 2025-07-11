// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class COUNT_MINIMUM_NUMBER_SUBSETS_SUBSEQUENCES_CONSECUTIVE_NUMBERS{
static int f_gold ( int arr [ ] , int n ) {
  Arrays . sort ( arr ) ;
  int count = 1 ;
  for ( int i = 0 ;
  i < n - 1 ;
  i ++ ) {
    if ( arr [ i ] + 1 != arr [ i + 1 ] ) count ++ ;
  }
  return count ;
}


static int f_filled ( int arr [ ] arr_size ) {
        Arrays.sort ( arr );
        int count = 1;
        for ( int i = 0 ; i < arr_size - 1 ; i++ ) {
            if ( arr [ i ] + 1!= arr [ i + 1 ] ) {
                count = count + 1;
            }
        }
        return count;
    }

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{3,7,7,11,14,14,14,16,17,17,21,22,24,27,27,27,31,33,35,36,36,37,38,43,45,49,52,54,57,59,59,60,67,73,74,74,74,75,75,79,83,87,90,93,97});
    param0.add(new int[]{-28,72,60,62,40,64,50,-36,-24,40,-6,78,-80,-82,2,-30,70,94,-2,-30,92,12,-46,32,-96,-2,36,-40,-42,66,98});
    param0.add(new int[]{1,1});
    param0.add(new int[]{96,89,24,28,70,78,78,35,98,65,18,81,35,91,33,88,69,52,66,17,73,79,30,33,78,60,42,8,36,6,47,87,8,98,9,77,78,24,86,91,13,79,50,85,3,7,61,94,86});
    param0.add(new int[]{-92,-92,-90,-84,-78,-66,-60,-60,-46,-42,-38,-32,-24,-20,-18,-16,-14,-10,0,4,6,12,24,32,34,44,48,50,50,64,66,68,80,84,86,86,88,90,90,90,92,94,96,98,98});
    param0.add(new int[]{0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,0,0});
    param0.add(new int[]{8,12,13,14,16,20,20,21,23,23,24,27,29,29,29,29,35,35,38,39,40,46,50,52,60,62,62,65,65,65,70,71,72,73,75,76,80,81,82,83,85,91,95,97,98,98});
    param0.add(new int[]{-84,92,70,-46,26,-94,-82,-26,-90,-62,52,62,-58,44,-14,-6,58,2,10,76,-34,42,-26,80,26,32,-82,38,2,72,68,44,24,84,-32,54,-96,-8,36,80,-82,32,98,-68});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{64,10,6,3,67,95,72,96,72,30,99,21,46,23,48,38,48,50,53,91,59,58,27,95,63,20,27,22,58,3,11,75,77,64,46,1,67,79,6,46,57,79,49,83,21,36,44});
    List<Integer> param1 = new ArrayList<>();
    param1.add(42);
    param1.add(24);
    param1.add(1);
    param1.add(26);
    param1.add(42);
    param1.add(27);
    param1.add(29);
    param1.add(25);
    param1.add(21);
    param1.add(46);
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