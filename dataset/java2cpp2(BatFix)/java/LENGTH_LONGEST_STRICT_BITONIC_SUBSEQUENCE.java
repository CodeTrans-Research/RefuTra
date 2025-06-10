int f_gold ( int arr [ ], int n ) {
  HashMap < Integer, Integer > inc = new HashMap < Integer, Integer > ( );
  HashMap < Integer, Integer > dcr = new HashMap < Integer, Integer > ( );
  int len_inc [ ] = new int [ n ];
  int len_dcr [ ] = new int [ n ];
  int longLen = 0;
  for ( int i = 0;
  i < n;
  i ++ ) {
    int len = 0;
    if ( inc . containsKey ( arr [ i ] - 1 ) ) len = inc . get ( arr [ i ] - 1 );
    len_inc [ i ] = len + 1;
    inc . put ( arr [ i ], len_inc [ i ] );
  }
  for ( int i = n - 1;
  i >= 0;
  i -- ) {
    int len = 0;
    if ( dcr . containsKey ( arr [ i ] - 1 ) ) len = dcr . get ( arr [ i ] - 1 );
    len_dcr [ i ] = len + 1;
    dcr . put ( arr [ i ], len_dcr [ i ] );
  }
  for ( int i = 0;
  i < n;
  i ++ ) if ( longLen < ( len_inc [ i ] + len_dcr [ i ] - 1 ) ) longLen = len_inc [ i ] + len_dcr [ i ] - 1;
  return longLen;
}