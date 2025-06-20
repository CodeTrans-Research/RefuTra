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
int f_gold ( int arr [ ], int n ) {
  int ans = 0;
  int maxele = * max_element ( arr, arr + n );
  for ( int i = 2;
  i <= maxele;
  ++ i ) {
    int count = 0;
    for ( int j = 0;
    j < n;
    ++ j ) {
      if ( arr [ j ] % i == 0 ) ++ count;
    }
    ans = max ( ans, count );
  }
  return ans;
}


int f_filled ( int arr [ ], int n ) {
  int ans = 0 ;
  int maxele = *max_element(arr, arr+n);
  for ( int i = 2 ; i <= maxele ; ++ i ) {
    int count = 0 ;
    for ( int j = 0 ; j < n ; ++ j ) {
      if ( arr [ j ] % i == 0 ) count++ ;
    }
    ans = max(ans, count) ;
  }
  return ans ;
}

int main() {
    int n_success = 0;
    vector<vector<int>> param0 {{10,18,22,22,22,29,30,32,33,34,37,39,40,41,44,47,49,50,50,51,53,67,69,70,71,71,73,75,78,80,81,82,91,91,93,97,97,99},{-42,62,6,98,38,-4,-38,72,42,4,-22,-94,78,-90,14},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{89,92,96,71,24,27,18,19,41,1,45,8},{-98,-94,-92,-90,-82,-80,-76,-76,-72,-62,-60,-58,-56,-52,-42,-36,-32,-32,-24,-22,-20,-10,-10,-10,-8,-2,-2,0,2,4,6,6,8,10,14,18,22,26,30,46,46,62,68,74,78,82,86,86},{1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,0,0,0,1,0,1,0,0,0,1},{4,8,10,10,11,17,18,25,32,33,34,37,40,41,44,47,47,52,63,77,85,87,89,89,91,95,96,98},{-86,52,-48,70,10,-94,16,14,38,62},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{95,32,87,37,86,71,30,88,96,52,88,92,79,86,19,5,74,67}};
    vector<int> param1 {35,10,23,7,40,41,23,9,30,13};
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