public static int f_gold(int n) {
    List<Integer> f = new ArrayList<>();
    f.add(0);
    f.add(1);
    f.add(1);

    for (int i = 3; i <= n; i++) {
        int r = f.get(f.get(i - 1)) + f.get(i - f.get(i - 1));
        f.add(r);
    }

    return f.get(n);
}
