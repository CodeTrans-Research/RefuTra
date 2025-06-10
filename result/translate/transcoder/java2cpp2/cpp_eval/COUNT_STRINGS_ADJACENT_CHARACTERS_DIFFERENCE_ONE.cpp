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
int f_gold ( int n ) {
  long int dp [ n + 1 ] [ 27 ];
  memset ( dp, 0, sizeof ( dp ) );
  for ( int i = 0;
  i <= 25;
  i ++ ) dp [ 1 ] [ i ] = 1;
  for ( int i = 2;
  i <= n;
  i ++ ) {
    for ( int j = 0;
    j <= 25;
    j ++ ) if ( j == 0 ) dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ];
    else dp [ i ] [ j ] = ( dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ] );
  }
  long int sum = 0;
  for ( int i = 0;
  i <= 25;
  i ++ ) sum = ( sum + dp [ n ] [ i ] );
  return sum;
}


long long f_filled ( int n ) {
  vector < vector < long long >> dp ( n + 1 , vector < long long > ( 27 , 0 ) ) ;
  for ( int i = 0 ;
  i < n + 1 ;
  i ++ ) {
    for ( int j = 0 ;
    j < 27 ;
    j ++ ) dp [ i ] [ j ] = 0 ;
  }
  for ( int i = 0 ;
  i <= 25 ;
  i ++ ) dp [ 1 ] [ i ] = 1 ;
  for ( int i = 2 ;
  i <= n ;
  i ++ ) {
    for ( int j = 0 ;
    j <= 25 ;
    j ++ ) {
      if ( j == 0 ) dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ] ;
      else dp [ i ] [ j ] = ( dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ] ) ;
    }
  }
  long long sum = 0 ;
  for ( int i = 0 ;
  i <= 25 ;
  i ++ ) sum = ( sum + dp [ n ] [ i ] ) ;
  return sum ;
}

int main() {
    int n_success = 0;
    vector<int> param0 {7,47,72,66,71,56,61,68,78,22};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0[i]) == f_gold(param0[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}