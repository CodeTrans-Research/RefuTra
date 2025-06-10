  boolean f_gold(int n) {
    return (!((n&0xAAAAAAAA)!=0) && ((n&(n-1))==0 && n!=0));
}
