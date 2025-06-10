int f_gold ( int arr [ ], int n ) {
    unordered_map<int,int> hm;
    for (int i=0;i<n;i++) {
        if (hm.find(arr[i])!=hm.end()) hm[arr[i]]++;
        else hm[arr[i]]=1;
    }
    int ans=0;
    for (auto it:hm) {
        int count=it.second;
        ans+=(count*(count-1))/2;
    }
    return ans;
}