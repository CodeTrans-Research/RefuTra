// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER{
static void f_gold ( int arr [ ] , int n ) {
  Vector < Integer > evenArr = new Vector < Integer > ( ) ;
  Vector < Integer > oddArr = new Vector < Integer > ( ) ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( i % 2 != 1 ) {
      evenArr . add ( arr [ i ] ) ;
    }
    else {
      oddArr . add ( arr [ i ] ) ;
    }
  }
  Collections . sort ( evenArr ) ;
  Collections . sort ( oddArr , Collections . reverseOrder ( ) ) ;
  int i = 0 ;
  for ( int j = 0 ;
  j < evenArr . size ( ) ;
  j ++ ) {
    arr [ i ++ ] = evenArr . get ( j ) ;
  }
  for ( int j = 0 ;
  j < oddArr . size ( ) ;
  j ++ ) {
    arr [ i ++ ] = oddArr . get ( j ) ;
  }
}


static void f_filled ( int [ ] arr , int n ) {
  int [ ] evenArr = new int [ n ] ;
  int [ ] oddArr = new int [ n ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( ( ( i % 2 ) == 0 ) && ( ( i % 2 ) == 1 ) ) {
      evenArr [ i ] = arr [ i ] ;
    }
    else {
      oddArr [ i ] = arr [ i ] ;
    }
  }
  Arrays . sort ( evenArr ) ;
  Arrays . sort ( oddArr ) ;
  oddArr [ 0 ] = 0 ;
  evenArr [ 1 ] = 0 ;
  oddArr [ 0 ] = 1 ;
  evenArr [ 2 ] = 0 ;
  oddArr [ 1 ] = 1 ;
  evenArr [ 3 ] = 0 ;
  evenArr [ 4 ] = 0 ;
  evenArr [ 5 ] = 0 ;
  evenArr [ 6 ] = 0 ;
  evenArr [ 7 ] = 0 ;
  evenArr [ 8 ] = 0 ;
  evenArr [ 9 ] = 0 ;
  evenArr [ 10 ] = 0 ;
  evenArr [ 11 ] = 0 ;
  evenArr [ 12 ] = 0 ;
  evenArr [ 13 ] = 0 ;
  evenArr [ 14 ] = 0 ;
  evenArr [ 15 ] = 0 ;
  evenArr [ 16 ] = 0 ;
  evenArr [ 17 ] = 0 ;
  evenArr [ 18 ] = 0 ;
  evenArr [ 19 ] = 0 ;
  evenArr [ 20 ] = 0 ;
  evenArr [ 21 ] = 0 ;
  evenArr [ 22 ] = 0 ;
  evenArr [ 23 ] = 0 ;
  evenArr [ 24 ] = 0 ;
  evenArr [ 25 ] = 0 ;
  evenArr [ 26 ] = 0 ;
  evenArr [ 27 ] = 0 ;
  evenArr [ 28 ] = 0 ;
  evenArr [ 29 ] = 0 ;
  evenArr [ 30 ] = 0 ;
  evenArr [ 31 ] = 0 ;
  evenArr [ 32 ] = 0 ;
  evenArr [ 33 ] = 0 ;
  evenArr [ 34 ] = 0 ;
  evenArr [ 35 ] = 0 ;
  evenArr [ 36 ] = 0 ;
  evenArr [ 37 ] = 0 ;
  evenArr [ 38 ] = 0 ;
  evenArr [ 39 ] = 0 ;
  evenArr [ 40 ] = 0 ;
  evenArr [ 41 ] = 0 ;
  evenArr [ 42 ] = 0 ;
  evenArr [ 43 ] = 0 ;
  evenArr [ 44 ] = 0 ;
  evenArr [ 45 ] = 0 ;
  evenArr [ 46 ] =

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{6,6,6,10,15,21,38,50,51,72,79,81,82,84,85,86,87});
    param0.add(new int[]{82,-36,18,-88,-24,20,26,-52,28,2});
    param0.add(new int[]{0,0,0,1,1,1});
    param0.add(new int[]{81,47,38,70,35,43,94,30,57,55,78,97,72,1});
    param0.add(new int[]{-80,-78,-72,-46,-26,-24,-20,8,16,26,38,44,54,68,68,78,86,92});
    param0.add(new int[]{0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,1,0,0,0});
    param0.add(new int[]{3,4,9,12,20,30,33,34,37,38,50,51,52,54,60,69,73,74,92,93,94,97,98});
    param0.add(new int[]{86,-32,64,-36,-36,-30,-66,-60,-76,-56,-60,-16,-60,-98,-18,72,-14});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{61,11,46,40,82,35,37,41,52,76,13,53,53,3,40,29,7,51,20,51,87,1,80,73,89,93,1,71,33,50,62,85,46,1,71,54,81,85});
    List<Integer> param1 = new ArrayList<>();
    param1.add(15);
    param1.add(7);
    param1.add(3);
    param1.add(8);
    param1.add(11);
    param1.add(21);
    param1.add(13);
    param1.add(10);
    param1.add(29);
    param1.add(36);
    List<int [ ]> filled_function_param0 = new ArrayList<>();
    filled_function_param0.add(new int[]{6,6,6,10,15,21,38,50,51,72,79,81,82,84,85,86,87});
    filled_function_param0.add(new int[]{82,-36,18,-88,-24,20,26,-52,28,2});
    filled_function_param0.add(new int[]{0,0,0,1,1,1});
    filled_function_param0.add(new int[]{81,47,38,70,35,43,94,30,57,55,78,97,72,1});
    filled_function_param0.add(new int[]{-80,-78,-72,-46,-26,-24,-20,8,16,26,38,44,54,68,68,78,86,92});
    filled_function_param0.add(new int[]{0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,1,0,0,0});
    filled_function_param0.add(new int[]{3,4,9,12,20,30,33,34,37,38,50,51,52,54,60,69,73,74,92,93,94,97,98});
    filled_function_param0.add(new int[]{86,-32,64,-36,-36,-30,-66,-60,-76,-56,-60,-16,-60,-98,-18,72,-14});
    filled_function_param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    filled_function_param0.add(new int[]{61,11,46,40,82,35,37,41,52,76,13,53,53,3,40,29,7,51,20,51,87,1,80,73,89,93,1,71,33,50,62,85,46,1,71,54,81,85});
    List<Integer> filled_function_param1 = new ArrayList<>();
    filled_function_param1.add(15);
    filled_function_param1.add(7);
    filled_function_param1.add(3);
    filled_function_param1.add(8);
    filled_function_param1.add(11);
    filled_function_param1.add(21);
    filled_function_param1.add(13);
    filled_function_param1.add(10);
    filled_function_param1.add(29);
    filled_function_param1.add(36);
    for(int i = 0; i < param0.size(); ++i)
    {
        f_filled(filled_function_param0.get(i),filled_function_param1.get(i));
        f_gold(param0.get(i),param1.get(i));
        for (int j=0; j<param0.get(i).length;j++){
            System.out.print(param0.get(i)[j]);
            System.out.print(" ");
        }
        System.out.println(param1.get(i));
        if(Arrays.equals(param0.get(i), filled_function_param0.get(i)) && param1.get(i) == filled_function_param1.get(i))
        {
            n_success+=1;
        }
    }
    System.out.println("#Results:" + n_success + ", " + param0.size());
}
}
