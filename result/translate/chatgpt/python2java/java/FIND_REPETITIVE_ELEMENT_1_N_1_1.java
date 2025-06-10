public int f_gold(int[] arr, int n) {
    HashSet<Integer> set = new HashSet<>();
    for(int i = 0; i < n; i++) {
        if(set.contains(arr[i])) {
            return arr[i];
        }
        set.add(arr[i]);
    }
    return -1;
}