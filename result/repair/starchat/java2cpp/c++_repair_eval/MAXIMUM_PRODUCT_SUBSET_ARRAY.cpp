// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;
int f_gold ( int a [ ], int n ) {
  if ( n == 1 ) return a [ 0 ];
  int max_neg = INT_MIN;
  int count_neg = 0, count_zero = 0;
  int prod = 1;
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( a [ i ] == 0 ) {
      count_zero ++;
      continue;
    }
    if ( a [ i ] < 0 ) {
      count_neg ++;
      max_neg = max ( max_neg, a [ i ] );
    }
    prod = prod + a [ i ];
  }
  if ( count_zero == n ) return 0;
  if ( count_neg & 1 ) {
    if ( count_neg == 1 && count_zero > 0 && count_zero + count_neg == n ) return 0;
    prod = prod / max_neg;
  }
  return prod;
}


int f_filled ( int a [ ], int n ) {
  if ( n == 1 ) {
    return a [ 0 ] ;
  }
  int max_neg = INT_MIN;
  int count_neg = 0, count_zero = 0 ;
  int prod = 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( a [ i ] == 0 ) {
      count_zero ++ ;
      continue ;
    }
    if ( a [ i ] < 0 ) {
      count_neg ++ ;
      max_neg = max ( max_neg, a [ i ] ) ;
    }
    prod = prod + a [ i ] ;
  }
  if ( count_zero == n ) {
    return 0 ;
  }
  if ( count_neg % 2 == 1 ) {
    if ( count_neg == 1 && count_zero > 0 && count_zero + count_neg == n ) {
      return 0 ;
    }
    prod = prod / max_neg ;
  }
  return prod ;
}

int main() {
    int n_success = 0;
    vector<vector<int>> param0 {{22,62,97},{-96,30,34,16,82,12,68,6,-2,-78,-74,-52,38,62,20,4,-32,44,-34,12,-44,-66,-94,24,-86,56,-20,-62,90,-16,-2,54,80,-16,-56,-98,20,84,30,-44,-78,66,-62,18},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{9,1,90,53,67,14,42,52,55,52,86,99,43,74,48,71,55,85,87,73,41,55,52},{-92,-78,-74,-72,-70,-66,-46,-44,-42,-34,-32,-30,-10,18,30,34,56,64,66},{0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0},{1,2,3,18,20,33,38,53,55,56,67,80,83,87,90,97,98},{-78,-14,20,70,-40,-96,78,70,-36,-30,24,-36,86,42,24,86,-52,-34,72,-58,-36,-24,-10,-68,-20,-64,34,42,-2,-8},{0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1},{1,6,32,4,63,85,48,64,11,29,77,59,1,99,17,17,38,49,78,82,50,87,75,18,75,73,98,17,27,51,4,98,96,6,74,5}};
    vector<int> param1 {2,41,43,20,10,16,9,16,11,32};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(&param0[i].front(),param1[i]) == f_gold(&param0[i].front(),param1[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}
