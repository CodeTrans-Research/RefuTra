int f_gold ( int arr [ ], int n ) {
      unordered_map < int, int > um;
      int max_dist = 0;
      for ( int i = 0; i < n; i++ ) {
        if (!um.count(arr[i])) um[arr[i]] = i;
        else max_dist = max(max_dist, i - um[arr[i]]);
      }
      return max_dist;
    }