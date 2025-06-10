int f_gold(int arr [],int n){
    unordered_map < int, pair < int, int > > um;
    for ( int i = 0; i < n - 1; i++ ) {
        for ( int j = i + 1; j < n; j++ ) {
            um[arr[i][j]] = {i, j};
        }
    }
    int ans = INT_MIN;
    for ( int i = 0; i < n; i++ ) {
        for ( int j = i + 1; j < n; j++ ) {
            int diff = abs(arr[i][j] - arr[i][i]);
            if ( um.find(diff)!= um.end() ) {
                if ( ( um[diff].first!= i && um[diff].first!= j ) && ( um[diff].second!= i && um[diff].second!= j ) ) {
                    ans = max(ans, max(arr[i][j], arr[i][i]));
                }
            }
        }
    }
    return ans;
}
