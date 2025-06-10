public static int f_gold(int s) {
    int length = s / 3;
    s -= length;
    int breadth = s / 2;
    int height = s - breadth;
    return (int) (length * breadth * height);
}