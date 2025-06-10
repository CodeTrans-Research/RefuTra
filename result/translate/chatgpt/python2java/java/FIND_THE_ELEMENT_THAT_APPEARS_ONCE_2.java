public static int f_gold(int[] a, int n) {
    int sum = 0;
    Set<Integer> set = new HashSet<>();
    
    for (int num : a) {
        set.add(num);
        sum += num;
    }
    
    return (3 * set.stream().mapToInt(Integer::intValue).sum() - sum) / 2;
}