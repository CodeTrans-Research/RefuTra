public int f_gold(String num) {
    int n = num.length();
    List<Integer> sumofdigit = new ArrayList<>();
    sumofdigit.add((int) num.charAt(0) - (int) '0');
    int res = sumofdigit.get(0);
    for(int i = 1; i < n; i++) {
        int numi = (int) num.charAt(i) - (int) '0';
        sumofdigit.add((i + 1) + numi + 10 + sumofdigit.get(i - 1));
        res += sumofdigit.get(i);
    }
    return res;
}