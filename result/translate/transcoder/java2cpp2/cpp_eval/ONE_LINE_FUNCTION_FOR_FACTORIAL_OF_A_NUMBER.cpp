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
  return ( n == 1 || n == 0 ) ? 1 : n * f_gold ( n - 1 );
}


int f_filled ( int n ) {
  return ( n == 1 || n == 0 ) ? 1 : n * f_filled ( n - 1 ) ;
}

int main() {
    int n_success = 0;
    vector<int> param0 {58,42,76,16,49,60,99,45,6,70};
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