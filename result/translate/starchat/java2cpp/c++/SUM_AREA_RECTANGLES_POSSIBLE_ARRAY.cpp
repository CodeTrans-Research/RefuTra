int f_gold ( int [ ] a, int n ) {
      a = vector<int>(a, a + n);
      sort(a.begin(), a.end());
      int sum = 0;
      bool flag = false;
      int len = 0;
      for (int i = 0; i < n - 1; i++) {
        if ((a[i] == a[i + 1] || a[i] - a[i + 1] == 1) &&!flag) {
          flag = true;
          len = a[i + 1];
          i++;
        } else if ((a[i] == a[i + 1] || a[i] - a[i + 1] == 1) && flag) {
          sum += a[i + 1] * len;
          flag = false;
          i++;
        }
      }
      return sum;
    }