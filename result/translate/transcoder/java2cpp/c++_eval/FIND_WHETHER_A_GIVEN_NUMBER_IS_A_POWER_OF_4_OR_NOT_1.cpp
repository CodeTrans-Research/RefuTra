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
  int count = 0;
  if ( n && ! ( n & ( n - 1 ) ) ) {
    while ( n > 1 ) {
      n >>= 1;
      count += 1;
    }
    return ( count % 2 == 0 ) ? true : false;
  }
  return false;
}


bool f_filled ( int n ) {
  int count = 0 ;
  int x = n & ( n - 1 ) ;
  if ( n > 0 && x == 0 ) {
    while ( n > 1 ) {
      n >>= 1 ;
      count += 1 ;
    }
    return ( count % 2 == 0 ) ? true : false ;
  }
  return false ;
}

int main() {
    int n_success = 0;
    vector<int> param0 {1,4,64,-64,128,1024,45,33,66,74};
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