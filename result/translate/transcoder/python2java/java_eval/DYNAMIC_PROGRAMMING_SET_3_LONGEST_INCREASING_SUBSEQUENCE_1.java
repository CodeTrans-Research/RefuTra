// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class DYNAMIC_PROGRAMMING_SET_3_LONGEST_INCREASING_SUBSEQUENCE_1{
static int f_gold ( int arr [ ] , int n ) {
  int f_gold [ ] = new int [ n ] ;
  int i , j , max = 0 ;
  for ( i = 0 ;
  i < n ;
  i ++ ) f_gold [ i ] = 1 ;
  for ( i = 1 ;
  i < n ;
  i ++ ) for ( j = 0 ;
  j < i ;
  j ++ ) if ( arr [ i ] > arr [ j ] && f_gold [ i ] < f_gold [ j ] + 1 ) f_gold [ i ] = f_gold [ j ] + 1 ;
  for ( i = 0 ;
  i < n ;
  i ++ ) if ( max < f_gold [ i ] ) max = f_gold [ i ] ;
  return max ;
}


static int f_filled ( int [ ] arr , int n ) {
  int [ ] lis = new int [ n ] ;
  lis [ 0 ] = 1 ;
  lis [ 1 ] = 0 ;
  lis [ 2 ] = 0 ;
  lis [ 3 ] = 0 ;
  lis [ 4 ] = 0 ;
  lis [ 5 ] = 0 ;
  lis [ 6 ] = 0 ;
  lis [ 7 ] = 0 ;
  lis [ 8 ] = 0 ;
  lis [ 9 ] = 0 ;
  lis [ 10 ] = 0 ;
  lis [ 11 ] = 0 ;
  lis [ 12 ] = 0 ;
  lis [ 13 ] = 0 ;
  lis [ 14 ] = 0 ;
  lis [ 15 ] = 0 ;
  lis [ 16 ] = 0 ;
  lis [ 17 ] = 0 ;
  lis [ 18 ] = 0 ;
  lis [ 19 ] = 0 ;
  lis [ 20 ] = 0 ;
  lis [ 21 ] = 0 ;
  lis [ 22 ] = 0 ;
  lis [ 23 ] = 0 ;
  lis [ 24 ] = 0 ;
  lis [ 25 ] = 0 ;
  lis [ 26 ] = 0 ;
  lis [ 27 ] = 0 ;
  lis [ 28 ] = 0 ;
  lis [ 29 ] = 0 ;
  lis [ 30 ] = 0 ;
  lis [ 31 ] = 0 ;
  lis [ 32 ] = 0 ;
  lis [ 33 ] = 0 ;
  lis [ 34 ] = 0 ;
  lis [ 35 ] = 0 ;
  lis [ 36 ] = 0 ;
  lis [ 37 ] = 0 ;
  lis [ 38 ] = 0 ;
  lis [ 39 ] = 0 ;
  lis [ 40 ] = 0 ;
  lis [ 41 ] = 0 ;
  lis [ 42 ] = 0 ;
  lis [ 43 ] = 0 ;
  lis [ 44 ] = 0 ;
  lis [ 45 ] = 0 ;
  lis [ 46 ] = 0 ;
  lis

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{2,3,5,6,8,12,12,17,17,18,22,22,26,26,31,31,31,31,32,35,35,38,41,42,49,49,60,60,61,63,64,68,69,70,71,72,76,77,80,83,83,89,90,90,90,96});
    param0.add(new int[]{-24,-16,-64,28,-30,-26,-14});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{11,42,44,52,15,35,48});
    param0.add(new int[]{-54});
    param0.add(new int[]{1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0});
    param0.add(new int[]{2,5,6,10,13,15,18,18,19,27,30,32,34,40,47,50,53,54,55,56,56,56,59,60,63,64,71,80,83,84,86,95});
    param0.add(new int[]{-80,60,-6,0,-50,82,-84,36,-96,-32,-14,16,60,-14,0,-22,28,12,8,-86,38,56,-32,-6,-80,-42,56,10,72,12,96,84});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{10,38,45,57,44,13,8,62,74,54,37,75,35,60,36,33,14,71,4,21,6,8,30,5,2,5,4,20,33,69,83,87,83,52,77,79,49,25,11,35,98,31,52,82,13,25,17,35,53});
    List<Integer> param1 = new ArrayList<>();
    param1.add(40);
    param1.add(4);
    param1.add(11);
    param1.add(6);
    param1.add(0);
    param1.add(22);
    param1.add(24);
    param1.add(16);
    param1.add(37);
    param1.add(28);
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