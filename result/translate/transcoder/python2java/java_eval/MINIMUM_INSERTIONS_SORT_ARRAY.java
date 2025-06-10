// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class MINIMUM_INSERTIONS_SORT_ARRAY{
static int f_gold ( int arr [ ] , int N ) {
  int [ ] lis = new int [ N ] ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) lis [ i ] = 1 ;
  for ( int i = 1 ;
  i < N ;
  i ++ ) for ( int j = 0 ;
  j < i ;
  j ++ ) if ( arr [ i ] >= arr [ j ] && lis [ i ] < lis [ j ] + 1 ) lis [ i ] = lis [ j ] + 1 ;
  int max = 0 ;
  for ( int i = 0 ;
  i < N ;
  i ++ ) if ( max < lis [ i ] ) max = lis [ i ] ;
  return ( N - max ) ;
}


static int f_filled ( int [ ] arr , int N ) {
  int lis [ ] = new int [ N ] ;
  lis [ 0 ] = 0 ;
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
  lis [ 47 ] = 0 ;
  lis [ 48 ] = 0 ;
  lis [ 49 ] = 0 ;
  lis [ 50 ] = 0 ;
  lis [ 51 ] = 0 ;
  lis [ 52 ] = 0 ;
  lis [ 53 ] = 0 ;
  lis [ 54 ] = 0 ;
  lis [ 55 ] = 0 ;
  lis [ 56 ] = 0 ;
  lis [ 57 ] = 0 ;
  lis [ 58 ] = 0 ;
  lis [ 59 ] = 0 ;

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{4,7,20,22,23,31,33,36,47,61,63,63,71,74,82,91,95,99});
    param0.add(new int[]{-84,12,-42,-78,22,72,56,70,28,-72});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{29,41,4,62,77,74,30,2,14,90,93,10,78,36,66,22,48,89,36,73,70,23,90});
    param0.add(new int[]{-80,-72,-68,-66,-58,-50,-48,-32,-28,-24,-22,-18,0,2,6,10,12,14,14,18,24,24,24,28,28,28,34,38,42,42,46,46,46,58,80,82,82,84,84,86,88,90,92,96});
    param0.add(new int[]{1,1,0,1,0,1,0,0,1,0});
    param0.add(new int[]{26,36,58,64,69,72,79,82,82,87,89,90,95});
    param0.add(new int[]{-52,-40,98,40,42,-50,60,-64,-92,36,-88,72,-72,38,-80,-52,68,70,16,22,-30,-74,56,-80,62,-54,-32,-22,-86,-70,88,-76,-46,28,40,-2,-84,68,-98,-16,90,36,-38,-86,20,-40,82,98,54});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{36,62,58,24,99,12,46,3,4,40,54,97,48,94,98,7,17,5,3,36,3});
    List<Integer> param1 = new ArrayList<>();
    param1.add(15);
    param1.add(7);
    param1.add(16);
    param1.add(13);
    param1.add(36);
    param1.add(8);
    param1.add(8);
    param1.add(41);
    param1.add(10);
    param1.add(16);
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