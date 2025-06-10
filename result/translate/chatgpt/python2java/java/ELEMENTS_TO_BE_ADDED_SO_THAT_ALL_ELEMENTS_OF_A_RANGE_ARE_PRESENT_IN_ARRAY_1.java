public static int f_gold(int [] arr, int n) {
    HashMap<Integer, Integer> s = new HashMap<>();
    int count = 0, maxm = -1000000000, minm = 1000000000;
    for(int i = 0; i < n; i++) {
        s.put(arr[i], 1);
        if(arr[i] < minm) {
            minm = arr[i];
        }
        if(arr[i] > maxm) {
            maxm = arr[i];
        }
    }
    for(int i = minm; i <= maxm; i++) {
        if(!s.containsKey(i)) {
            count++;
        }
    }
    return count;
}