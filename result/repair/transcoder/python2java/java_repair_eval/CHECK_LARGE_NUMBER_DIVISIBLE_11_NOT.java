// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class CHECK_LARGE_NUMBER_DIVISIBLE_11_NOT{
static boolean f_gold ( String str ) {
  int n = str . length ( ) ;
  int oddDigSum = 0 , evenDigSum = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( i % 2 == 0 ) oddDigSum += ( str . charAt ( i ) - '0' ) ;
    else evenDigSum += ( str . charAt ( i ) - '0' ) ;
  }
  return ( ( oddDigSum - evenDigSum ) % 11 == 0 ) ;
}


static boolean f_filled ( String str ) {
  int n = str . length ( ) ;
  int oddDigSum = 0 ;
  int evenDigSum = 0 ;
for (int i=0;i<n;i++){
    if ( ( i % 2 == 0 ) && ( i % 3 == 0 ) ) oddDigSum = oddDigSum + ( Character . digit ( str . charAt ( i ) , 16 ) - 48 ) ;
    else evenDigSum = evenDigSum + ( Character . digit ( str . charAt ( i ) , 16 ) - 48 ) ;
  }
  return ( ( oddDigSum - evenDigSum ) % 11 == 0 ) ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<String> param0 = new ArrayList<>();
    param0.add("r");
    param0.add("7386620");
    param0.add("1010");
    param0.add("rWFOLX VB");
    param0.add("3845847974820");
    param0.add("01001");
    param0.add("yq");
    param0.add("770356");
    param0.add("0000110111001");
    param0.add("tDMrBdHJJITDx");
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