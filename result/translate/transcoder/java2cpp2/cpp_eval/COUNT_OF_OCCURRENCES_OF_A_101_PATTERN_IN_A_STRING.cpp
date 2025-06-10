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
int f_gold ( string str ) {
  int len = str . size ( );
  bool oneSeen = 0;
  int count = 0;
  for ( int i = 0;
  i < len;
  i ++ ) {
    if ( str [ i ] == '1' && oneSeen == 1 ) if ( str [ i - 1 ] == '0' ) count ++;
    if ( str [ i ] == '1' && oneSeen == 0 ) {
      oneSeen = 1;
      continue;
    }
    if ( str [ i ] != '0' && str [ i ] != '1' ) oneSeen = 0;
  }
  return count;
}


int f_filled ( string str ) {
  int len = str . length ( ) ;
  bool one_seen = false ;
  int count = 0 ;
  for ( int i = 0 ;
  i < len ;
  i ++ ) {
    char getChar = str [ i ] ;
    if ( getChar == '1' && one_seen == true ) {
      if ( str [ i - 1 ] == '0' ) {
        count ++ ;
      }
    }
    if ( getChar == '1' && one_seen == false ) {
      one_seen = true ;
    }
    if ( getChar != '0' && str [ i ] != '1' ) {
      one_seen = false ;
    }
  }
  return count ;
}

int main() {
    int n_success = 0;
    vector<string> param0 {"1001ab010abc01001","1001010001","010100010100","DLCu","7072430592","011","pnJpypYOza","1037","111","HxK"};
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