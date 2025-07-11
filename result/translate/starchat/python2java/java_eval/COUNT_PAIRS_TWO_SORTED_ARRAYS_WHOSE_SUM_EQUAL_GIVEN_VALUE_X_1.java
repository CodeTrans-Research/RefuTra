// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X_1{
static int f_gold ( int arr1 [ ] , int arr2 [ ] , int m , int n , int x ) {
  int count = 0 ;
  HashSet < Integer > us = new HashSet < Integer > ( ) ;
  for ( int i = 0 ;
  i < m ;
  i ++ ) us . add ( arr1 [ i ] ) ;
  for ( int j = 0 ;
  j < n ;
  j ++ ) if ( us . contains ( x - arr2 [ j ] ) ) count ++ ;
  return count ;
}


static int f_filled ( int arr1 [ ], int arr2 [ ], int m, int n, int x ) {
        Set < Integer > us = new HashSet < > ( );
        for ( int i = 0 ; i < m ; i ++ ) us.add ( arr1 [ i ] );
        int count = 0;
        for ( int j = 0 ; j < n ; j ++ ) if ( x - arr2 [ j ] in us ) count ++;
        return count;
    }

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{1,2,5,5,9,11,12,14,16,18,35,36,39,44,50,52,52,59,69,81,82,84,85,87,87,87,88,88,89,90,90,92,97});
    param0.add(new int[]{52,28,-38,78,-86,78,-48,-70,-80,28,-8,60,-28,90,6,76,32,-54,30,30,-32,-24,-36,62,36,-66,56,92,-20,90,32});
    param0.add(new int[]{0,0,0,0,0,0,0,0,1,1,1,1,1,1,1});
    param0.add(new int[]{91,95,13,13,76,18,36,86,26,13,17,68,58,42,38,9,42,90,14,74,38,64,15});
    param0.add(new int[]{-96,-94,-94,-92,-74,-70,-66,-54,-48,-20,-18,-10,-6,-2,2,18,36,48,52,58,68,74,88,90,94});
    param0.add(new int[]{1,1,1,0,0,0,1,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,1,0});
    param0.add(new int[]{7,18,19,20,24,25,25,27,30,35,39,42,58,59,63,64,64,66,66,68,69,77,86,93});
    param0.add(new int[]{86,44,10,80,12,52,-92,2,42,-32,-14,2,-42,40,96,22,58,-90,-20,22,96,10,-92,-28,-28,80,36,72,-2,32,-46,62,-58,20,22,32,-98,-2,-42,-90,10,70,54,-32});
    param0.add(new int[]{0,0,1,1,1,1});
    param0.add(new int[]{43,2,4,99,45,80,27,8,64,77,57,55,71,67,51,42,58,70,5,62,55,20,61,47,66,80,70,24,56,22,58,63,61,41,20,97,47});
    List<int [ ]> param1 = new ArrayList<>();
    param1.add(new int[]{5,5,8,20,20,24,25,29,34,37,43,45,48,49,59,60,68,70,70,72,72,75,76,77,79,81,84,85,86,88,95,96,96});
    param1.add(new int[]{-88,-32,30,32,-46,62,-92,-90,-18,-18,10,16,60,-40,32,-88,60,-82,76,50,86,-82,-48,-68,-42,34,4,0,98,92,-78});
    param1.add(new int[]{0,0,0,0,0,0,0,1,1,1,1,1,1,1,1});
    param1.add(new int[]{16,96,8,35,12,27,81,21,32,82,95,81,53,76,72,16,9,16,61,1,36,71,28});
    param1.add(new int[]{-92,-72,-72,-64,-58,-52,-30,-28,-24,-24,-16,-10,-2,4,12,22,30,38,44,62,64,68,86,88,90});
    param1.add(new int[]{1,0,1,1,1,0,0,0,0,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,1,0,0});
    param1.add(new int[]{2,2,18,20,22,22,31,35,36,40,41,41,41,42,42,43,45,61,79,83,87,91,95,96});
    param1.add(new int[]{-4,-76,-98,14,30,-10,-10,62,88,-94,-74,-82,84,44,58,8,-42,-66,-18,68,-78,42,-32,38,-98,38,-78,42,86,-38,-6,-72,-44,8,-6,-48,-62,82,94,-92,-56,28,-54,34});
    param1.add(new int[]{0,0,1,1,1,1});
    param1.add(new int[]{11,66,41,17,93,25,24,17,12,33,62,86,48,68,36,36,39,82,7,66,5,48,27,9,56,6,61,91,98,74,61,63,98,96,57,63,85});
    List<Integer> param2 = new ArrayList<>();
    param2.add(17);
    param2.add(30);
    param2.add(13);
    param2.add(11);
    param2.add(19);
    param2.add(18);
    param2.add(22);
    param2.add(26);
    param2.add(5);
    param2.add(24);
    List<Integer> param3 = new ArrayList<>();
    param3.add(29);
    param3.add(27);
    param3.add(11);
    param3.add(12);
    param3.add(14);
    param3.add(19);
    param3.add(18);
    param3.add(36);
    param3.add(3);
    param3.add(29);
    List<Integer> param4 = new ArrayList<>();
    param4.add(32);
    param4.add(17);
    param4.add(8);
    param4.add(15);
    param4.add(21);
    param4.add(29);
    param4.add(18);
    param4.add(31);
    param4.add(5);
    param4.add(21);
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i),param1.get(i),param2.get(i),param3.get(i),param4.get(i)) == f_gold(param0.get(i),param1.get(i),param2.get(i),param3.get(i),param4.get(i)))
        {
            n_success+=1;
        }
    }
    System.out.println("#Results:" + n_success + ", " + param0.size());
}
}