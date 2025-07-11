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
bool f_gold ( unsigned int n ) {
  return n != 0 && ( ( n & ( n - 1 ) ) == 0 ) && ! ( n & 0xAAAAAAAA );
}


bool f_filled ( unsigned n ) {
  return n != 0 && ( ( n & ( n - 1 ) ) == 0 ) && ( n & 0xAAAAAAAA ) == 0 ;
}

int main() {
    int n_success = 0;
    vector<int> param0 {1,4,64,-64,128,1024,97,86,14,99};
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