std::string f_gold(std::string s) {
  int n = s.length();
  int sub_count = n * (n + 1) / 2;
  std::string* arr = new std::string[sub_count];
  int index = 0;
  for (int i = 0; i < n; i++) {
    for (int len = 1; len <= n - i; len++) {
      arr[index++] = s.substr(i, len);
    }
  }
  std::sort(arr, arr + sub_count);
  std::string res = "";
  for (int i = 0; i < sub_count; i++) {
    res += arr[i];
  }
  delete[] arr;
  return res;
}