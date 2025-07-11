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
int f_gold ( int W, int wt [ ], int val [ ], int n ) {
  if ( n == 0 || W == 0 ) return 0;
  if ( wt [ n - 1 ] > W ) return f_gold ( W, wt, val, n - 1 );
  else return max ( val [ n - 1 ] + f_gold ( W - wt [ n - 1 ], wt, val, n - 1 ), f_gold ( W, wt, val, n - 1 ) );
}


int f_filled ( int W , int wt [ ] , int val [ ] , int n ) {
  if ( n == 0 || W == 0 ) return 0 ;
  if ( wt [ n - 1 ] > W ) return f_filled ( W , wt , val , n - 1 ) ;
  else return max ( val [ n - 1 ] + f_filled ( W - wt [ n - 1 ] , wt , val , n - 1 ) , f_filled ( W , wt , val , n - 1 ) ) ;
}

int main() {
    int n_success = 0;
    vector<int> param0 {5,9,26,7,46,28,25,9,13,4};
    vector<vector<int>> param1 {{6,14,18,36,40,47,54,58},{42,60,-4,24,54,42,-72,-92,48,-94,-36,18},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1},{56,53,85,73,93,75,21,22,39,13,92},{-96,-96,-94,-84,-78,-76,-74,-74,-72,-70,-70,-50,-48,-38,-30,-28,-28,-24,-14,-10,-4,-2,6,6,18,28,30,30,34,36,42,48,50,52,54,58,58,60,62,74,74,86,86,88,88,94,96,96,98},{1,1,0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0},{7,16,18,21,22,26,30,32,34,37,37,38,39,40,44,54,55,56,56,58,59,60,62,62,64,66,75,80,82,83,84,85,88,89,89,90,93,96,97},{64,-38,76,-24,-10,78,-76,78,-32,20},{0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1},{10,87,55,78,11}};
    vector<vector<int>> param2 {{9,15,23,24,41,45,50,92},{-20,56,20,-82,84,-90,54,50,82,92,-32,6},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1},{17,27,34,86,49,89,79,70,32,23,64},{-92,-72,-72,-68,-60,-58,-52,-48,-46,-46,-44,-44,-42,-36,-32,-30,-30,-24,-22,-18,-16,-8,-6,-6,-4,-2,6,8,16,20,20,30,32,32,36,40,42,44,44,46,54,56,56,58,82,82,86,90,90},{1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0},{1,7,9,10,11,21,23,25,29,32,35,35,35,36,37,38,42,47,47,48,51,52,55,58,64,70,72,73,74,76,77,80,86,91,92,92,92,92,96},{64,50,-78,78,78,44,-14,-70,-76,90},{0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1},{29,43,93,2,42}};
    vector<int> param3 {7,7,15,9,28,21,31,6,14,2};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0[i],&param1[i].front(),&param2[i].front(),param3[i]) == f_gold(param0[i],&param1[i].front(),&param2[i].front(),param3[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}