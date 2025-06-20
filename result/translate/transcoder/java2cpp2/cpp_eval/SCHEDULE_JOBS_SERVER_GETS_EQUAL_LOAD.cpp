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
int f_gold ( int a [ ], int b [ ], int n ) {
  int i;
  long long int s = 0;
  for ( i = 0;
  i < n;
  i ++ ) s += ( a [ i ] + b [ i ] );
  if ( n == 1 ) return a [ 0 ] + b [ 0 ];
  if ( s % n != 0 ) return - 1;
  int x = s / n;
  for ( i = 0;
  i < n;
  i ++ ) {
    if ( a [ i ] > x ) return - 1;
    if ( i > 0 ) {
      a [ i ] += b [ i - 1 ];
      b [ i - 1 ] = 0;
    }
    if ( a [ i ] == x ) continue;
    int y = a [ i ] + b [ i ];
    if ( i + 1 < n ) y += b [ i + 1 ];
    if ( y == x ) {
      a [ i ] = y;
      b [ i ] = b [ i + 1 ] = 0;
      continue;
    }
    if ( a [ i ] + b [ i ] == x ) {
      a [ i ] += b [ i ];
      b [ i ] = 0;
      continue;
    }
    if ( i + 1 < n && a [ i ] + b [ i + 1 ] == x ) {
      a [ i ] += b [ i + 1 ];
      b [ i + 1 ] = 0;
      continue;
    }
    return - 1;
  }
  for ( i = 0;
  i < n;
  i ++ ) if ( b [ i ] != 0 ) return - 1;
  return x;
}


int f_filled ( int a [ ] , int b [ ] , int n ) {
  int i ;
  int s = 0 ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    s += ( a [ i ] + b [ i ] ) ;
  }
  if ( n == 1 ) return a [ 0 ] + b [ 0 ] ;
  if ( s % n != 0 ) return - 1 ;
  int x = s / n ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    if ( a [ i ] > x ) return - 1 ;
    if ( i > 0 ) {
      a [ i ] += b [ i - 1 ] ;
      b [ i - 1 ] = 0 ;
    }
    if ( a [ i ] == x ) continue ;
    int y = a [ i ] + b [ i ] ;
    if ( i + 1 < n ) y += b [ i + 1 ] ;
    if ( y == x ) {
      a [ i ] = y ;
      b [ i ] = 0 ;
      continue ;
    }
    if ( a [ i ] + b [ i ] == x ) {
      a [ i ] += b [ i ] ;
      b [ i ] = 0 ;
      continue ;
    }
    if ( i + 1 < n && a [ i ] + b [ i + 1 ] == x ) {
      a [ i ] += b [ i + 1 ] ;
      b [ i + 1 ] = 0 ;
      continue ;
    }
    return - 1 ;
  }
  for ( i = 0 ;
  i < n ;
  i ++ ) if ( b [ i ] != 0 ) return - 1 ;
  return x ;
}

int main() {
    int n_success = 0;
    vector<vector<int>> param0 {{4,9,16,18,20,23,24,25,25,26,29,30,35,40,41,43,44,46,53,53,56,56,58,60,62,70,80,80,80,82,86,90,92,92,95},{-24,70,-74,-90,72,50,-94,86,-58,-68,42,0,98,-70,-14,-32,6,74,64,-78,86,-42,-56,2,-34,-46,70,-62,50,-58,-58,42,86,96,-8,8,-22,-14,-14,98,2,98,-28},{0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1},{98,18,50,36,88,75,2,40,74,19,63,82,77,5,59,97,70,50,71,90,90,61,63,99},{-80,-64,-64,-64,-64,-62,-54,-48,-44,-44,-38,-30,-30,-26,-14,-12,-10,-6,-6,6,22,22,22,26,28,50,52,70,86,86,88,90},{0,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0,1},{59,61,64},{98,92,28,42,-74,-36,40,-8,32,-22,-70,-22,-56,74,6,6,-62,46,34,2},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{72,97,79,21,83,2,31,59,6,11,79,97}};
    vector<vector<int>> param1 {{3,15,16,16,18,26,30,32,32,35,37,41,42,43,48,49,49,54,55,57,65,66,67,67,68,83,85,89,89,90,91,93,96,97,99},{-26,36,48,48,-38,-86,90,-62,30,-4,82,16,32,-6,58,82,-66,-40,52,-78,94,-70,-80,-68,-58,-26,50,-78,-90,-48,-28,48,56,50,72,-22,-2,8,-94,92,-44,-66,-30},{0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1},{93,25,16,42,55,61,69,68,95,28,40,90,1,86,76,40,13,47,71,4,64,54,84,45},{-96,-94,-80,-74,-64,-56,-52,-32,-30,-24,-12,-12,-8,-2,4,8,16,20,24,24,24,48,50,54,60,64,74,80,88,90,92,92},{1,1,1,0,1,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1},{22,59,85},{-62,-84,72,60,10,-18,-44,-22,14,0,76,72,96,-28,-24,52,-74,-30,16,66},{0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{27,71,87,36,73,37,80,34,57,17,88,52}};
    vector<int> param2 {29,34,13,16,22,20,1,18,34,9};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(&param0[i].front(),&param1[i].front(),param2[i]) == f_gold(&param0[i].front(),&param1[i].front(),param2[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}