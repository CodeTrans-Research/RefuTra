// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class FIND_PAIR_MAXIMUM_GCD_ARRAY{
public static int f_gold ( int arr [ ] , int n ) {
  int high = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) high = Math . max ( high , arr [ i ] ) ;
  int divisors [ ] = new int [ high + 1 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 1 ;
    j <= Math . sqrt ( arr [ i ] ) ;
    j ++ ) {
      if ( arr [ i ] % j == 0 ) {
        divisors [ j ] ++ ;
        if ( j != arr [ i ] / j ) divisors [ arr [ i ] / j ] ++ ;
      }
    }
  }
  for ( int i = high ;
  i >= 1 ;
  i -- ) if ( divisors [ i ] > 1 ) return i ;
  return 1 ;
}


static int f_filled ( int arr [ ], int n ) {
    int high = 0, i = 0;
    while ( i < n ) {
        high = Math.max ( high, arr [ i ] );
        i++;
    }
    int divisors [ ] = new int [ high + 1 ];
    i = 0;
    while ( i < n ) {
        int j = 1;
        while ( j <= (int) Math.sqrt ( arr [ i ] ) ) {
            if ( arr [ i ] % j == 0 ) {
                divisors [ j ] = divisors [ j ] + 1;
                if ( j!= arr [ i ] / j ) divisors [ arr [ i ] / j ] = divisors [ arr [ i ] / j ] + 1;
            }
            j++;
        }
        i++;
    }
    i = high;
    while ( i >= 1 ) {
        if ( divisors [ i ] > 1 ) return i;
        i--;
    }
    return 1;
}

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{3,3,8,10,12,13,14,16,16,19,20,21,25,29,33,35,35,35,35,36,38,41,42,45,45,45,46,48,51,52,53,55,56,57,58,62,69,73,73,76,76,80,89,91,92,93,93,96});
    param0.add(new int[]{12,52,-66,50,50,-78,-14,26,56,74,8,-58,58,-66,-58,-12,80});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{23,98,12,45,83,85,30,92,26,12,38,20,86,52,71,20,56,78,10,34,86,55,99,84,26,2,1,89,60,26,16,37,98,11,73,42,36,60,28});
    param0.add(new int[]{-98,-84,-80,-72,-66,-64,-52,-36,-28,-18,-12,-12,-4,8,12,40,42,56,68,70,90,94});
    param0.add(new int[]{1,0,0,1,1,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,0,1,0,0,1,0,1});
    param0.add(new int[]{3,5,6,7,8,9,11,13,18,20,24,25,26,27,36,41,41,45,48,48,49,65,69,70,85,90,99,99});
    param0.add(new int[]{80,-26,-38,-40,22,-28,0,-36,70,-32,38,58,76,-42,38,92,68,-70,36,-62,24,-84,42,4,0,8,-36,98,-84,82,-70,-12,6,-82,-20,-68,48,-12,42,18,58,-14,94,84});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{36,60,45,76,43,71,10,18,52,52,53,73,48,95,13,50,97,30,73,13,18,34,51});
    List<Integer> param1 = new ArrayList<>();
    param1.add(45);
    param1.add(11);
    param1.add(26);
    param1.add(28);
    param1.add(17);
    param1.add(14);
    param1.add(20);
    param1.add(39);
    param1.add(26);
    param1.add(22);
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