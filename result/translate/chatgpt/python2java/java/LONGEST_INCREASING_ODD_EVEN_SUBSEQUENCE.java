public static int f_gold(int[] arr, int n) {
    List<Integer> lioes = new ArrayList<>();
    int maxLen = 0;
    for (int i = 0; i < n; i++) {
        lioes.add(1);
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] > arr[j] && (arr[i] + arr[j]) % 2 != 0 && lioes.get(i) < lioes.get(j) + 1) {
                lioes.set(i, lioes.get(j) + 1);
            }
        }
    }

    for (int i = 0; i < n; i++) {
        if (maxLen < lioes.get(i)) {
            maxLen = lioes.get(i);
        }
    }

    return maxLen;
}