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
double f_gold ( int n ) {
  return ( 3.0 * n ) / ( 4.0 * ( n * n ) - 1 );
}


double f_filled(int n) {
    return (3.0 * n) / (4.0 * (n * n) - 1);
}

int main() {
    int n_success = 0;
    vector<int> param0 {46,5,44,15,72,2,86,17,30,42};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(abs(1 - (0.0000001 + abs(f_gold(param0[i])) )/ (abs(f_filled(param0[i])) + 0.0000001)) < 0.001)
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}