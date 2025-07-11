// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class FIND_INDEX_OF_AN_EXTRA_ELEMENT_PRESENT_IN_ONE_SORTED_ARRAY{
static int f_gold ( int arr1 [ ] , int arr2 [ ] , int n ) {
  for ( int i = 0 ;
  i < n ;
  i ++ ) if ( arr1 [ i ] != arr2 [ i ] ) return i ;
  return n ;
}


static int f_filled ( int [ ] arr1 , int [ ] arr2 , int n ) {
  for ( int i = 0 ;
  i != n ;
  i ++ ) {
    if ( ( arr1 [ i ] != arr2 [ i ] ) && ( arr1 [ i ] != arr2 [ i ] ) ) {
      return i ;
    }
  }
  return n ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{1,6,7,10,11,12,12,16,17,29,32,33,35,35,45,49,52,56,57,58,61,62,63,64,68,71,71,77,79,79,81,82,82,83,83,89,89,93,94,94});
    param0.add(new int[]{-48,-92,96,-18,10,-24,-4,96,-16,-78,4,-80,-96,-28,-78,68,2,-60,0});
    param0.add(new int[]{1});
    param0.add(new int[]{68,98,21,29,71,49});
    param0.add(new int[]{-80,-76,-76,-76,-68,-66,-56,-44,-38,-28,-24,-10,8,14,16,18,24,26,30,32,50,64,76,80,90,94,94,94});
    param0.add(new int[]{0,0,1,0,1,0,1,1,1,1,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,1,1,0,1});
    param0.add(new int[]{3,7,16,17,20,22,29,32,34,34,35,40,40,40,41,46,49,58,60,62,63,64,64,68,70,73,76,79,83,86,90,92,99});
    param0.add(new int[]{18,-68,-6,-32,-76,-86,-8,76,-46,20,-80,54,-88,-58,-48,-66,-66,18,-28,-74,-72,-26,-92,-78,24,-22,-80,-80,82,-2,-72,-88,-54,-84,-8});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{74,75,52,58,34,53,51,45,34,28,53,94,10,20,23,12,95,78,48,11});
    List<int [ ]> param1 = new ArrayList<>();
    param1.add(new int[]{3,12,13,14,15,17,18,19,22,24,28,29,33,37,41,42,44,49,51,51,52,53,56,56,59,60,64,64,67,70,71,78,83,88,88,90,92,93,93,95});
    param1.add(new int[]{-38,-40,-50,50,-26,-80,64,54,74,-44,-40,-92,-16,4,-60,-42,-60,-74,38});
    param1.add(new int[]{0});
    param1.add(new int[]{97,90,25,89,57,41});
    param1.add(new int[]{-90,-88,-66,-60,-48,-48,-46,-42,-40,-36,-26,-4,2,4,4,8,16,18,34,50,52,56,64,80,86,90,92,96});
    param1.add(new int[]{0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0,1});
    param1.add(new int[]{4,4,7,13,23,23,25,25,26,34,38,39,39,45,48,50,52,54,58,59,60,65,72,76,80,80,80,84,87,90,92,94,96});
    param1.add(new int[]{-30,96,92,-12,-14,-68,-16,20,74,-42,36,84,-82,66,44,70,-92,-56,-28,-68,-4,10,-4,90,72,84,68,14,32,60,40,60,-34,58,-56});
    param1.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param1.add(new int[]{62,56,17,1,11,30,59,18,99,21,86,49,24,85,25,56,21,66,23,96});
    List<Integer> param2 = new ArrayList<>();
    param2.add(36);
    param2.add(16);
    param2.add(0);
    param2.add(3);
    param2.add(14);
    param2.add(22);
    param2.add(26);
    param2.add(17);
    param2.add(24);
    param2.add(17);
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i),param1.get(i),param2.get(i)) == f_gold(param0.get(i),param1.get(i),param2.get(i)))
        {
            n_success+=1;
        }
    }
    System.out.println("#Results:" + n_success + ", " + param0.size());
}
}