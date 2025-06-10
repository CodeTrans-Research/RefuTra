public void f_gold(int arr[], int n) {
    List<Integer> evenArr = new ArrayList<>();
    List<Integer> oddArr = new ArrayList<>();
    for (int i = 0; i < n; i++) {
        if ((i % 2) == 0) {
            evenArr.add(arr[i]);
        } else {
            oddArr.add(arr[i]);
        }
    }
    Collections.sort(evenArr);
    Collections.sort(oddArr);
    Collections.reverse(oddArr);
    int i = 0;
    for (int j = 0; j < evenArr.size(); j++) {
        arr[i] = evenArr.get(j);
        i++;
    }
    for (int j = 0; j < oddArr.size(); j++) {
        arr[i] = oddArr.get(j);
        i++;
    }
}