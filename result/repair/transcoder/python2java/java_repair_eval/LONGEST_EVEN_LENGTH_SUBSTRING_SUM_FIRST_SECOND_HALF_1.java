// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_1{
static int f_gold ( String str ) {
  int n = str . length ( ) ;
  int maxlen = 0 ;
  int sum [ ] [ ] = new int [ n ] [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) sum [ i ] [ i ] = str . charAt ( i ) - '0' ;
  for ( int len = 2 ;
  len <= n ;
  len ++ ) {
    for ( int i = 0 ;
    i < n - len + 1 ;
    i ++ ) {
      int j = i + len - 1 ;
      int k = len / 2 ;
      sum [ i ] [ j ] = sum [ i ] [ j - k ] + sum [ j - k + 1 ] [ j ] ;
      if ( len % 2 == 0 && sum [ i ] [ j - k ] == sum [ ( j - k + 1 ) ] [ j ] && len > maxlen ) maxlen = len ;
    }
  }
  return maxlen ;
}


static int f_filled ( String string ) {
  int n = string . length ( ) ;
  int maxlen = 0 ;
  int [ ] [ ] Sum = new int [ n ] [ n ] ;
for (int i=0;i<n;i++){
    Sum [ i ] [ i ] = Integer . parseInt ( string . substring ( i , i + 1 ) ) ;
  }
  for ( int length = 2 ;
  length <= n ;
  length ++ ) {
for (int i=0;i<n-length+1;i++){
      int j = i + length - 1 ;
      int k = length / 2 ;
      Sum [ i ] [ j ] = ( Sum [ i ] [ j - k ] + Sum [ j - k + 1 ] [ j ] ) ;
      if ( ( length % 2 == 0 && Sum [ i ] [ j - k ] == Sum [ ( j - k + 1 ) ] [ j ] && length > maxlen ) || ( length % 2 == 0 && Sum [ i ] [ j - k ] == Sum [ ( j - k + 1 ) ] [ j ] && length > maxlen ) ) {
        maxlen = length ;
      }
    }
  }
  return maxlen ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("jNkTf");
    param0.add("7");
    param0.add("100001101001");
    param0.add("fRXyQrTUjEk");
    param0.add("908404");
    param0.add("0101010010");
    param0.add("svq");
    param0.add("19");
    param0.add("11100010001");
    param0.add("O HgwJyOVfnV");
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