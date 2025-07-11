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
void f_gold ( int arr [ ], int n ) {
  int max_ele = arr [ n - 1 ];
  int min_ele = arr [ 0 ];
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( i % 2 == 0 ) {
      arr [ i ] = max_ele;
      max_ele -= 1;
    }
    else {
      arr [ i ] = min_ele;
      min_ele += 1;
    }
  }
}


void f_filled ( int arr [ ] , int n ) {
  int max_ele = arr [ n - 1 ] ;
  int min_ele = arr [ 0 ] ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( i % 2 == 0 ) {
      arr [ i ] = max_ele ;
      max_ele -= 1 ;
    }
    else {
      arr [ i ] = min_ele ;
      min_ele += 1 ;
    }
  }
}

int main() {
    int n_success = 0;
    vector<vector<int>> param0 {{3,4,8,10,12,14,14,17,18,19,20,25,28,29,30,31,34,35,37,38,40,41,42,45,47,49,54,54,55,58,58,63,65,66,66,67,67,72,74,75,75,80,82,86,92,95,96,99},{45,42,-91,90,-6,49,65,39,-80,-65,-47,75,10,80,36,-96,55,72,68,2,-53,-6,72,-52,-9,80,-16,-32,39,25,-27,-96,-24,-27,-23,-52},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{12,84,16},{-85,-77,-70,-67,-55,-51,-49,-41,-37,-24,-18,-8,-6,77,87,90},{0,0,1,1,1,1,1,1,1,0,1,1,0,0,0},{5,8,15,16,20,22,25,33,46,48,52,54,55,57,57,61,61,66,72,73,83,87,88,89,98},{31,2,-46,-86,-64,5,-18,-33,-90,-51,11,-35,-43,-73,13,33,-29,-17,-43,20,-7,-85},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{20,75,12,62,18,94,63,84,25,12}};
    vector<int> param1 {40,23,28,2,13,12,12,13,31,9};
    vector<vector<int>> filled_function_param0 {{3,4,8,10,12,14,14,17,18,19,20,25,28,29,30,31,34,35,37,38,40,41,42,45,47,49,54,54,55,58,58,63,65,66,66,67,67,72,74,75,75,80,82,86,92,95,96,99},{45,42,-91,90,-6,49,65,39,-80,-65,-47,75,10,80,36,-96,55,72,68,2,-53,-6,72,-52,-9,80,-16,-32,39,25,-27,-96,-24,-27,-23,-52},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{12,84,16},{-85,-77,-70,-67,-55,-51,-49,-41,-37,-24,-18,-8,-6,77,87,90},{0,0,1,1,1,1,1,1,1,0,1,1,0,0,0},{5,8,15,16,20,22,25,33,46,48,52,54,55,57,57,61,61,66,72,73,83,87,88,89,98},{31,2,-46,-86,-64,5,-18,-33,-90,-51,11,-35,-43,-73,13,33,-29,-17,-43,20,-7,-85},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{20,75,12,62,18,94,63,84,25,12}};
    vector<int> filled_function_param1 {40,23,28,2,13,12,12,13,31,9};
    for(int i = 0; i < param0.size(); ++i)
    {
        f_filled(&filled_function_param0[i].front(),filled_function_param1[i]);
        f_gold(&param0[i].front(),param1[i]);
        if(equal(begin(param0[i]), end(param0[i]), begin(filled_function_param0[i])) && param1[i] == filled_function_param1[i])
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}