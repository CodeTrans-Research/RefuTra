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
int f_gold ( int arr [ ], int n, int x ) {
  int i;
  for ( i = 0;
  i < n;
  i ++ ) {
    if ( arr [ i ] == x ) return i;
  }
  return - 1;
}


int f_filled ( int arr [ ], int n, int x ) {
  int i ;
  for ( i = 0 ;
  i < n ;
  i ++ ) {
    if ( arr [ i ] == x ) {
      return i ;
    }
  }
  return - 1 ;
}

int main() {
    int n_success = 0;
    vector<vector<int>> param0 {{4,5,5,11,13,14,15,19,22,22,23,26,29,29,36,44,48,49,65,65,67,68,70,76,79,79,81,85,88,91,91,92,92,97},{-24,-78,-32,-48,0,4,-42},{0,0,0,0,0,0,0,1,1,1,1},{38,14,75,16,91,11,98,43,67,9,21,10,82,72,32,81,48,60,2,91,10,90,12,83},{-92,-92,-82,-80,-76,-66,-64,-64,-56,-48,-38,-38,-34,-32,-32,-10,-8,-6,-2,0,8,10,18,20,22,22,30,34,38,38,38,44,50,52,56,64,64,66,70,76,88},{0,1,1,0,0,1,1,0,0,0,1,1,1,1},{1,4,4,4,4,8,12,13,14,14,22,25,25,27,29,33,36,38,40,40,40,41,47,47,47,48,48,50,51,52,52,52,55,56,59,59,62,64,66,77,82,84,90,91,91,93},{-90,-60,-58,-72,92,54,-32,-70,-94,18,64,-90,-90,-56,82,-14,-74,-96,-90,-8,-48,76,-28,10,-52,-8,-46,-32,82,46,58,92,4,48,-96,-66,60,60,62,-68},{0,0,0,0,0,0,1,1,1,1},{42,17,77,96,72,36,74,97,7,94,80,7,27,58,49,81,51,9}};
    vector<int> param1 {17,4,6,17,25,11,38,22,8,16};
    vector<int> param2 {5,0,0,75,25,-1,4,22,8,11};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(&param0[i].front(),param1[i],param2[i]) == f_gold(&param0[i].front(),param1[i],param2[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}