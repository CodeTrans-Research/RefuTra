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
  int C [ n + 1 ] [ n + 1 ];
  int i, j;
  for ( i = 0;
  i <= n;
  i ++ ) {
    for ( j = 0;
    j <= min ( i, n );
    j ++ ) {
      if ( j == 0 || j == i ) C [ i ] [ j ] = 1;
      else C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ];
    }
  }
  int sum = 0;
  for ( int i = 0;
  i <= n;
  i ++ ) sum += ( C [ n ] [ i ] * C [ n ] [ i ] );
  return sum;
}


int f_filled(int n) {
    int** C = new int*[n + 1];
    for (int i = 0; i <= n; i++) {
        C[i] = new int[n + 1];
    }
    int i, j;
    for (i = 0; i <= n; i++) {
        for (j = 0; j <= std::min(i, n); j++) {
            if (j == 0 || j == i) C[i][j] = 1;
            else C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }
    int sum = 0;
    for (i = 0; i <= n; i++) sum += (C[n][i] * C[n][i]);
    return sum;
}

int main() {
    int n_success = 0;
    vector<int> param0 {57,44,19,24,64,60,57,22,15,63};
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