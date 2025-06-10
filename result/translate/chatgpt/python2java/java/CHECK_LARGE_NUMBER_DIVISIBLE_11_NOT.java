public static boolean f_gold(String str) {
    int n = str.length();
    int oddDigSum = 0;
    int evenDigSum = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            oddDigSum = oddDigSum + (str.charAt(i) - '0');
        } else {
            evenDigSum = evenDigSum + (str.charAt(i) - '0');
        }
    }
    return ((oddDigSum - evenDigSum) % 11 == 0);
}