public static int f_gold(String tree, int k) {
    int level = -1;
    int sum = 0;
    int n = tree.length();
    for (int i = 0; i < n; i++) {
        if (tree.charAt(i) == '(') {
            level += 1;
        } else if (tree.charAt(i) == ')') {
            level -= 1;
        } else {
            if (level == k) {
                sum += (tree.charAt(i) - '0');
            }
        }
    }
    return sum;
}