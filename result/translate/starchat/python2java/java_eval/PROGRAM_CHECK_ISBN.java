// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class PROGRAM_CHECK_ISBN{
static boolean f_gold ( String isbn ) {
  int n = isbn . length ( ) ;
  if ( n != 10 ) return false ;
  int sum = 0 ;
  for ( int i = 0 ;
  i < 9 ;
  i ++ ) {
    int digit = isbn . charAt ( i ) - '0' ;
    if ( 0 > digit || 9 < digit ) return false ;
    sum += ( digit * ( 10 - i ) ) ;
  }
  char last = isbn . charAt ( 9 ) ;
  if ( last != 'X' && ( last < '0' || last > '9' ) ) return false ;
  sum += ( ( last == 'X' ) ? 10 : ( last - '0' ) ) ;
  return ( sum % 11 == 0 ) ;
}


static boolean f_filled ( String isbn ) {
    if (isbn.length()!= 10) return false;
    int sum = 0;
    for (int i = 0; i < 9; i++) {
        if (isbn.charAt(i) >= '0' && isbn.charAt(i) <= '9')
            sum += (isbn.charAt(i) - '0') * (10 - i);
        else
            return false;
    }
    if (isbn.charAt(9) == 'X') sum += 10;
    else if (isbn.charAt(9) >= '0' && isbn.charAt(9) <= '9') sum += (isbn.charAt(9) - '0');
    else return false;
    return (sum % 11 == 0);
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("007462542X");
    param0.add("0112112425");
    param0.add("0545010225");
    param0.add("0552527408");
    param0.add("424519151311");
    param0.add("101011");
    param0.add("9780552527408");
    param0.add("2290344397");
    param0.add("1473226406");
    param0.add("DDdguSGiRr");
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