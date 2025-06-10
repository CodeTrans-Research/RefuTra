public static String f_gold(String seq) {
    int n = seq.length();
    if (n >= 9) {
        return "-1";
    }
    String[] result = new String[n + 1];
    Arrays.fill(result, "");
    int count = 1;
    for (int i = 0; i < n + 1; i++) {
        if (i == n || seq.charAt(i) == 'I') {
            for (int j = i - 1; j >= -1; j--) {
                result[j + 1] = String.valueOf((char) ('0' + count));
                count++;
                if (j >= 0 && seq.charAt(j) == 'I') {
                    break;
                }
            }
        }
    }
    return String.join("", result);
}