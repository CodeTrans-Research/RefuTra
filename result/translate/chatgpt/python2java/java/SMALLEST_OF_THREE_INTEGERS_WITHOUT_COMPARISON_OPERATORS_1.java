public static int f_gold(int x, int y, int z){
    if((int)(y / x) == 0){
        return !((int)(y / z) == 0) ? z : y;
    }
    return !((int)(x / z) == 0) ? z : x;
}