public int f_gold(String n) {
    int res = Integer.parseInt(n);
    for (int j = n.length() - 1; j >= 0; j--) {
        res += Character.getNumericValue(n.charAt(j));
    }
    return res;
}