// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class CHECK_LARGE_NUMBER_DIVISIBLE_13_NOT{
static boolean f_gold ( String num ) {
  int length = num . length ( ) ;
  if ( length == 1 && num . charAt ( 0 ) == '0' ) return true ;
  if ( length % 3 == 1 ) {
    num += "00" ;
    length += 2 ;
  }
  else if ( length % 3 == 2 ) {
    num += "0" ;
    length += 1 ;
  }
  int sum = 0 , p = 1 ;
  for ( int i = length - 1 ;
  i >= 0 ;
  i -- ) {
    int group = 0 ;
    group += num . charAt ( i -- ) - '0' ;
    group += ( num . charAt ( i -- ) - '0' ) * 10 ;
    group += ( num . charAt ( i ) - '0' ) * 100 ;
    sum = sum + group * p ;
    p *= ( - 1 ) ;
  }
  sum = Math . abs ( sum ) ;
  return ( sum % 13 == 0 ) ;
}


static boolean f_filled ( String num ) {
  int length = num . length ( ) ;
  if ( ( length == 1 && num . charAt ( 0 ) == '0' ) || ( length == 2 && num . charAt ( 0 ) == '1' ) ) return true ;
  if ( ( length % 3 == 1 ) || ( length % 3 == 2 ) ) {
    num = String . format ( "%s%s" , num , "00" ) ;
    length += 2 ;
  }
  else if ( ( length % 3 == 2 ) || ( length % 3 == 3 ) ) {
    num = String . format ( "%s%s" , num , "0" ) ;
    length += 1 ;
  }
  double sum = 0 ;
  double p = 1 ;
  for ( int i = length - 1 ;
  i >= 0 ;
  i -- ) {
    double group = 0 ;
    group += ( int ) num . charAt ( i ) - '0' ;
    i -- ;
    group  =group + (((int)(num.charAt(i))-(int)('0'))*10);
    i -- ;
    group  =group + (((int)(num.charAt(i))-(int)('0'))*100);
    sum = sum + group * p ;
    p *= ( - 1 ) ;
  }
  sum = Math . abs ( sum ) ;
  return ( sum % 13 == 0 ) ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("vzTUaItpCpLnjY");
    param0.add("33855");
    param0.add("0011110101011");
    param0.add("MMQ");
    param0.add("439340517954");
    param0.add("000000000");
    param0.add("UugAuRRJbjEgl");
    param0.add("6406553695441");
    param0.add("011001");
    param0.add("yjFqEEvgiNjEX");
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