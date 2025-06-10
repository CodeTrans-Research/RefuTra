// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class NUMBER_N_DIGIT_STEPPING_NUMBERS{
static long f_gold ( int n ) {
  int dp [ ] [ ] = new int [ n + 1 ] [ 10 ] ;
  if ( n == 1 ) return 10 ;
  for ( int j = 0 ;
  j <= 9 ;
  j ++ ) dp [ 1 ] [ j ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= 9 ;
    j ++ ) {
      if ( j == 0 ) dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ] ;
      else if ( j == 9 ) dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ] ;
      else dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ] ;
    }
  }
  long sum = 0 ;
  for ( int j = 1 ;
  j <= 9 ;
  j ++ ) sum += dp [ n ] [ j ] ;
  return sum ;
}


static int f_filled ( int n ) {
  int [ ] [ ] dp = new int [ 10 ] [ n + 1 ] ;
  for ( int y = 0 ;
  y < n ;
  y ++ ) {
    dp [ y ] [ 0 ] = 0 ;
    dp [ y ] [ 1 ] = y ;
  }
  ;
  if ( ( n == 1 ) && ( n == 10 ) ) {
    return 10 ;
  }
  ;
  for ( int j = 0 ;
  j < 10 ;
  j ++ ) {
    dp [ 1 ] [ j ] = 1 ;
    dp [ 2 ] [ j ] = 1 ;
    dp [ 3 ] [ j ] = 1 ;
    dp [ 4 ] [ j ] = 1 ;
    dp [ 5 ] [ j ] = 1 ;
    dp [ 6 ] [ j ] = 1 ;
    dp [ 7 ] [ j ] = 1 ;
    dp [ 8 ] [ j ] = 1 ;
    dp [ 9 ] [ j ] = 1 ;
    dp [ 10 ] [ j ] = 1 ;
    dp [ 11 ] [ j ] = 1 ;
    dp [ 12 ] [ j ] = 1 ;
    dp [ 13 ] [ j ] = 1 ;
    dp [ 14 ] [ j ] = 1 ;
    dp [ 15 ] [ j ] = 1 ;
    dp [ 16 ] [ j ] = 1 ;
    dp [ 17 ] [ j ] = 1 ;
    dp [ 18 ] [ j ] = 1 ;
    dp [ 19 ] [ j ] = 1 ;
    dp [ 20 ] [ j ] = 1 ;
    dp [ 21 ] [ j ] = 1 ;
    dp [ 22 ] [ j ] = 1 ;
    dp [ 23 ] [ j ] = 1 ;
    dp [ 24 ] [ j ] = 1 ;
    dp [ 25 ] [ j ] = 1 ;
    dp [ 26 ] [ j ] = 1 ;
    dp [ 27 ] [ j ] = 1 ;
    dp [ 28 ] [ j ] = 1 ;
    dp [ 29 ] [ j ] = 1 ;
    dp [ 30 ] [ j ] = 1 ;
    dp [ 31 ] [ j ] = 1 ;
    dp [ 32 ] [ j ] = 1 ;
    dp [ 33 ] [ j ] = 1 ;
    dp [ 34 ] [ j ] = 1 ;
    dp [ 35 ] [ j ] = 1 ;
    dp [ 36 ] [ j ] = 1 ;
    dp [ 37 ] [ j ] = 1 ;
    dp [ 38 ] [ j ] = 1 ;
    dp [ 39 ] [ j ] = 1 ;
    dp [ 40 ] [ j ] = 1 ;
    dp [ 41 ] [ j ] = 1 ;

public static void main(String args[]) {
    int n_success = 0;
    List<Integer> param0 = new ArrayList<>();
    param0.add(18);
    param0.add(16);
    param0.add(13);
    param0.add(10);
    param0.add(26);
    param0.add(11);
    param0.add(20);
    param0.add(25);
    param0.add(12);
    param0.add(13);
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
