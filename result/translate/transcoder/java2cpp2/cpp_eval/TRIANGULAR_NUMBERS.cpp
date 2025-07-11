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
bool f_gold ( int num ) {
  if ( num < 0 ) return false;
  int sum = 0;
  for ( int n = 1;
  sum <= num;
  n ++ ) {
    sum = sum + n;
    if ( sum == num ) return true;
  }
  return false;
}


bool f_filled ( int num ) {
  if ( num < 0 ) return false ;
  int sum = 0 ;
  for ( int n = 1 ;
  sum <= num ;
  n ++ ) {
    sum = sum + n ;
    if ( sum == num ) return true ;
  }
  return false ;
}

int main() {
    int n_success = 0;
    vector<int> param0 {97,97,32,40,18,14,90,39,1,57};
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