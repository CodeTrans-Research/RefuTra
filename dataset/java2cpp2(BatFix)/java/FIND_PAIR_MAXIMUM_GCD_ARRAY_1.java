class A{

static int f_gold ( int arr [ ], int n ) {
  int high = 0;
  for ( int i = 0;
  i < n;
  i ++ )
    high = Math . max ( high, arr [ i ] );
  int count [ ] = new int [ high + 1 ];
  for ( int i = 0;
  i < n;
  i ++ )
    count [ arr [ i ] ] ++;
  int counter = 0;
  for ( int i = high;
  i >= 1;
  i -- ) {
    int j = i;
    while ( j <= high ) {
      if ( count [ j ] > 0 )
        counter += count [ j ];
      j += i;
      if ( counter == 2 )
        return i;
    }
    counter = 0;
  }
  return 1;
}
public static void main(String[] a){
  int arr[] = {-56,94,84,14,-6,84,84,-14,-60,-50,38,-20,66,-16};
  int b =  8;
  System.out.println(f_gold(arr,b));
}
}