int f_gold ( int arr [ ], int n ) {
    unordered_map<int,int> mp;
    for (int i=0;i<n;i++) mp[arr[i]]++;
set<int> ans = 0;
    for (auto x:mp) if (x.second==1) ans++;
    return n-ans;
}
