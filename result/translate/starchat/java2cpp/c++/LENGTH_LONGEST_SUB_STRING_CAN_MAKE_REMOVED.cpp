int f_gold ( string str ) {
    vector < pair < char, int > > arr;
    arr.push_back(make_pair('@', -1));
    int maxlen = 0;
    for (int i = 0; i < str.length(); i++) {
        arr.push_back(make_pair(str[i], i));
        while (arr.size() >= 3 && arr[arr.size() - 3].first == '1' && arr[arr.size() - 2].first == '0' && arr[arr.size() - 1].first == '0') {
            arr.pop_back();
            arr.pop_back();
            arr.pop_back();
        }
        int tmp = arr[arr.size() - 1].second;
        maxlen = max(maxlen, i - tmp);
    }
    return maxlen;
}