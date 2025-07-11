// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class SMALLEST_DIFFERENCE_PAIR_VALUES_TWO_UNSORTED_ARRAYS{
static int f_gold ( int A [ ] , int B [ ] , int m , int n ) {
  A = Arrays.copyOfRange( A , 0 , m );
  B = Arrays.copyOfRange( B , 0 , n );
  Arrays . sort ( A ) ;
  Arrays . sort ( B ) ;
  int a = 0 , b = 0 ;
  int result = Integer . MAX_VALUE ;
  while ( a < m && b < n ) {
    if ( Math . abs ( A [ a ] - B [ b ] ) < result ) result = Math . abs ( A [ a ] - B [ b ] ) ;
    if ( A [ a ] < B [ b ] ) a ++ ;
    else b ++ ;
  }
  return result ;
}


static int f_filled ( int [ ] A , int [ ] B , int m , int n ) {
  A = A . clone ( ) ;
  B = B . clone ( ) ;
  A . sort ( ) ;
  B . sort ( ) ;
  int a = 0 ;
  int b = 0 ;
  int result = Integer . MAX_VALUE ;
  while (a<m&&b<n){
    if ( ( Math . abs ( A [ a ] - B [ b ] ) < result ) || ( Math . abs ( A [ a ] - B [ b ] ) < result ) ) {
      result = Math . abs ( A [ a ] - B [ b ] ) ;
    }
    if (A[a] < B[b]) {
      a ++ ;
    }
    else {
      b ++ ;
    }
  }
  return result ;
}

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{2,2,11,13,18,18,23,25,28,28,37,39,53,56,67,70,74,74,75,79,80,82,84,89,94,95,95,98,98});
    param0.add(new int[]{-78,10,-8,30,-70,-94,-48,-4,-22,-40,-36,-48,-4,86,-50,62,-72,-44,-62,22,-30,-72,6,-24,-78,72,-44,56,38,-36,0,-72,-10,-12,-70,-64,-24});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{57,82,90,9,61,71,15,2,39,24,28,28,47});
    param0.add(new int[]{-92,-90,-90,-28,-16,-14,-14,-8,42,52,62,84});
    param0.add(new int[]{1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,1,0,0,1,1,0,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0});
    param0.add(new int[]{6,7,7,12,15,15,21,24,26,26,28,36,38,42,46,52,55,56,59,62,63,65,65,66,68,71,73,77,77,77,77,85,87,87,88,90,93,94,98});
    param0.add(new int[]{-68,44,88,-68,22,34,-82,18,-60,30,24,18,78,90,-20,-60,94,70,4,-16,-38});
    param0.add(new int[]{0,0,1});
    param0.add(new int[]{14,7,9,71,37,20,85,62,70,67,26,47,61,99,2,90,70,46,53,16,56,7,15,81,85,94,73,40,35,58,21,98,45});
    List<int [ ]> param1 = new ArrayList<>();
    param1.add(new int[]{5,6,11,13,13,16,17,19,23,25,28,31,31,39,41,44,45,52,62,64,70,71,73,78,78,79,85,86,92});
    param1.add(new int[]{78,-80,-24,-50,-26,-62,26,-12,22,-90,84,10,18,62,26,-68,92,64,-52,76,-84,64,50,36,-24,-98,42,72,-78,-98,-24,86,2,60,-30,14,-42});
    param1.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1});
    param1.add(new int[]{85,92,84,27,54,77,26,49,47,51,70,11,41});
    param1.add(new int[]{-98,-98,-58,-6,14,16,18,46,52,52,52,56});
    param1.add(new int[]{0,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,0,1});
    param1.add(new int[]{1,3,4,4,6,7,8,8,15,17,18,18,20,23,23,24,25,25,26,33,39,43,46,54,59,67,69,69,69,69,76,76,81,81,85,86,86,91,95});
    param1.add(new int[]{-18,-30,-74,-50,98,-44,-62,-20,18,84,62,-64,-2,62,-32,-34,-14,-52,-36,-60,-68});
    param1.add(new int[]{0,0,1});
    param1.add(new int[]{99,72,29,55,88,1,88,19,7,80,79,18,28,41,48,49,67,27,24,94,86,14,45,84,37,71,92,98,16,64,67,44,29});
    List<Integer> param2 = new ArrayList<>();
    param2.add(28);
    param2.add(23);
    param2.add(14);
    param2.add(7);
    param2.add(11);
    param2.add(35);
    param2.add(30);
    param2.add(16);
    param2.add(2);
    param2.add(20);
    List<Integer> param3 = new ArrayList<>();
    param3.add(14);
    param3.add(33);
    param3.add(16);
    param3.add(8);
    param3.add(6);
    param3.add(33);
    param3.add(20);
    param3.add(12);
    param3.add(1);
    param3.add(25);
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i),param1.get(i),param2.get(i),param3.get(i)) == f_gold(param0.get(i),param1.get(i),param2.get(i),param3.get(i)))
        {
            n_success+=1;
        }
    }
    System.out.println("#Results:" + n_success + ", " + param0.size());
}
}
