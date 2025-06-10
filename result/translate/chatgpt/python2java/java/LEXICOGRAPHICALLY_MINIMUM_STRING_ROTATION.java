public String f_gold(String str_) {
    int n = str_.length();
    String[] arr = new String[n];
    String concat = str_ + str_;
    for(int i = 0; i < n; i++) {
        arr[i] = concat.substring(i, n + i);
    }
    Arrays.sort(arr);
    return arr[0];
}