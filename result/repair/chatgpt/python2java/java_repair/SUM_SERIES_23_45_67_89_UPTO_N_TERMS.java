  double f_gold(int n) {
    int i = 1;
    double res = 0.0;
    boolean sign = true;
    while (n > 0) {
        n = n - 1;
        if (sign) {
            sign = false;
            res =  res+(double)(i+1)/(i+2);
            i = i + 2;
        } else {
            sign = true;
            res =  res-(double)(i+1)/(i+2);
            i = i + 2;
        }
    }
    return res;
}
