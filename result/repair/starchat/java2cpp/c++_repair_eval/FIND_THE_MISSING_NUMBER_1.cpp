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
int f_gold ( int a [ ], int n ) {
  int i, total = 1;
  for ( i = 2;
  i <= ( n + 1 );
  i ++ ) {
    total += i;
    total -= a [ i - 2 ];
  }
  return total;
}


int f_filled ( int a [ ], int n ) {
  int total = 1 ;
  for (int i=2;i<(n+1)+1;i++){
    total += i ;
    total -= a [ i - 2 ] ;
  }
  return total ;
}

int main() {
    int n_success = 0;
    vector<vector<int>> param0 {{13,27,46,59,62,82,92},{22,86,-64,-20,-56,-16,86,42,72,-90,10,42,56,8,50,24,-34,0,-78,64,18,20,-84,-22,90,-20,86,26,-54,0,90,-48,4,88,18,-64,-22,-74,48,-36,-86,-24,88,-64,68,62,92},{0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1},{55,89,56,85,26,4,91,91,3,77,63,59,76,90,1,94,44,70,8,54,3,91,29,95,28,75,20},{-94,-84,-80,-78,-66,-62,-54,-52,-26,-8,-8,-6,4,4,8,14,26,58,60,62,62,76,78,86,92},{1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0},{1,2,7,7,9,14,23,29,31,31,35,35,38,41,44,49,49,50,51,54,55,56,57,63,67,69,73,79,79,80,86,88,93},{78,-48,16,22,-16,34,56,-20,-62,-82,-74,-40,20,-24,-46,64,66,-76,58,-84,96,76,86,-32,46},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{73,76,25,59,40,85,90,38,13,97,93,99,45,7}};
    vector<int> param1 {6,38,15,22,18,25,24,12,29,12};
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