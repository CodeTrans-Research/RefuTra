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
string f_gold ( string str ) {
  stack < int > integerstack;
  stack < char > stringstack;
  string temp = "", result = "";
  for ( int i = 0;
  i < str . length ( );
  i ++ ) {
    int count = 0;
    if ( str [ i ] >= '0' && str [ i ] <= '9' ) {
      while ( str [ i ] >= '0' && str [ i ] <= '9' ) {
        count = count * 10 + str [ i ] - '0';
        i ++;
      }
      i --;
      integerstack . push ( count );
    }
    else if ( str [ i ] == ']' ) {
      temp = "";
      count = 0;
      if ( ! integerstack . empty ( ) ) {
        count = integerstack . top ( );
        integerstack . pop ( );
      }
      while ( ! stringstack . empty ( ) && stringstack . top ( ) != '[' ) {
        temp = stringstack . top ( ) + temp;
        stringstack . pop ( );
      }
      if ( ! stringstack . empty ( ) && stringstack . top ( ) == '[' ) stringstack . pop ( );
      for ( int j = 0;
      j < count;
      j ++ ) result = result + temp;
      for ( int j = 0;
      j < result . length ( );
      j ++ ) stringstack . push ( result [ j ] );
      result = "";
    }
    else if ( str [ i ] == '[' ) {
      if ( str [ i - 1 ] >= '0' && str [ i - 1 ] <= '9' ) stringstack . push ( str [ i ] );
      else {
        stringstack . push ( str [ i ] );
        integerstack . push ( 1 );
      }
    }
    else stringstack . push ( str [ i ] );
  }
  while ( ! stringstack . empty ( ) ) {
    result = stringstack . top ( ) + result;
    stringstack . pop ( );
  }
  return result;
}


string f_filled ( string str ) {
    stack < int > s;
    stack < char > st;
    string res;
    string temp;
    for ( int i = 0; i < str. length(); i++ ) {
        if ( isdigit( str[i] ) ) {
            int num = 0;
            while ( isdigit( str[i] ) ) {
                num = num * 10 + str[i] - '0';
                i++;
            }
            i--;
            s.push( num );
        }
        else if ( str[i] == ']' ) {
            if (!s.empty() ) {
                int count = s.top();
                s.pop();
            }
            while (!st.empty() && st.top()!= '[' ) {
                temp = st.top() + temp;
                st.pop();
            }
            if (!st.empty() && st.top() == '[' ) st.pop();
            for ( int j = 0; j < count; j++ ) res += temp;
            for ( int j = 0; j < res.length(); j++ ) st.push( res[j] );
            res = "";

int main() {
    int n_success = 0;
    vector<string> param0 {"rpaBQkHqRaTb","9916267","000010100010","XfHXbWwaRd","750","0","K","0218044","10100010011","zR"};
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