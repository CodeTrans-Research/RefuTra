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
int f_gold ( int arr [ ], int arr_size ) {
  for ( int i = 0;
  i < arr_size;
  i ++ ) {
    int count = 0;
    for ( int j = 0;
    j < arr_size;
    j ++ ) {
      if ( arr [ i ] == arr [ j ] ) count ++;
    }
    if ( count % 2 != 0 ) return arr [ i ];
  }
  return - 1;
}


int f_filled(int arr[], int arr_size) {
    int i;
    for (i = 0; i < arr_size; i++) {
        int count = 0;
        for (int j = 0; j < arr_size; j++) {
            if (arr[i] == arr[j]) count++;
        }
        if (count % 2 != 0) return arr[i];
    }
    return -1;
}

int main() {
    int n_success = 0;
    vector<vector<int>> param0 {{1,5,5,8,14,15,17,17,18,23,23,25,26,35,36,39,51,53,56,56,60,62,64,64,65,66,67,68,71,75,80,82,83,88,89,91,91,92,93,95,99},{-56,98,44,30,-88,18,60,86,4,16,10,64,-22,-86,-66,-16,70,-44,98,78,-96,-66,92,10,40,-16},{0,0,0,0,0,1,1,1},{36,11,83,41,42,14,46,89,91,96,57,42,74,73,9,26,79,40,31,69,44,39,14,92,34,20,52,47,14},{-84,-84,-84,-78,-66,-62,-62,-36,-24,-10,-10,-8,-4,-2,12,14,20,22,36,42,46,66,84,96,96,98},{1,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,1,1,1,0,1,1,1,1,1,1},{11,12,14,28,42,48,50,58,67,74,86,89,95},{52,-56,-6,74,10,68,74,10,16,-80,82,-32,6,-6,82,20},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{4,80,92}};
    vector<int> param1 {31,19,6,25,23,19,7,11,31,1};
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