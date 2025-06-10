bool f_gold(int n){
    if(n == 0 || n == 9) return true;
    if(n < 9) return false;
    return f_gold((int)(n >> 3) - (int)(n & 7));
}