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
int f_gold ( int x ) {
  return ( 3 * x * ( x + 1 ) ) / 2;
}


int f_filled ( int x ) {
  return ( 3 * x * ( x + 1 ) ) / 2 ;
}

int main() {
    int n_success = 0;
    vector<int> param0 {6,25,15,30,17,80,27,13,12,67};
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