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
  int pPrevPrev = 1, pPrev = 1, pCurr = 1, pNext = 1;
  for ( int i = 3;
  i <= n;
  i ++ ) {
    pNext = pPrevPrev + pPrev;
    pPrevPrev = pPrev;
    pPrev = pCurr;
    pCurr = pNext;
  }
  return pNext;
}


int f_filled ( int n ) {
  int pPrevPrev = 1 , pPrev = 1 , pCurr = 1 , pNext = 1 ;
  for ( int i = 3 ;
  i <= n ;
  i ++ ) {
    pNext = pPrevPrev + pPrev ;
    pPrevPrev = pPrev ;
    pPrev = pCurr ;
    pCurr = pNext ;
  }
  return pNext ;
}

int main() {
    int n_success = 0;
    vector<int> param0 {1,92,29,52,55,13,83,83,10,67};
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