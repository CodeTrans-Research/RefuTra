int f_gold ( int x, int y, int z ) {
    int count = 0;
    while (x!= 0 && y!= 0 && z!= 0) {
        x--;
        y--;
        z--;
        count++;
    }
    return count;
}