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
  int dp [ n + 1 ];
  dp [ 0 ] = 0, dp [ 1 ] = 1;
  for ( int i = 2;
  i <= n;
  i ++ ) dp [ i ] = max ( dp [ i / 2 ] + dp [ i / 3 ] + dp [ i / 4 ], i );
  return dp [ n ];
}


int f_filled(int n) {
    int* dp = new int[n + 1];
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = std::max(dp[i / 2] + dp[i / 3] + dp[i / 4], i);
    }
    return dp[n];
}

int main() {
    int n_success = 0;
    vector<int> param0 {50,83,18,24,31,38,94,24,13,53};
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