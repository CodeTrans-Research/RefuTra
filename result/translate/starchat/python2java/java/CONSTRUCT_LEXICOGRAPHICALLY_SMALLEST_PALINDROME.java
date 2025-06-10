public static String f_gold ( String s, int l ) {
        char[] arr = s.toCharArray();
        int i = 0, j = l - 1;
        while (i < j) {
            if (arr[i] == arr[j] && arr[i]!= '*') {
                i++;
                j--;
            } else if (arr[i] == arr[j] && arr[i] == '*') {
                arr[i] = 'a';
                arr[j] = 'a';
                i++;
                j--;
            } else if (arr[i] == '*') {
                arr[i] = arr[j];
                i++;
            } else if (arr[j] == '*') {
                arr[j] = arr[i];
                j--;
            } else {
                return "Not Possible";
            }
        }
        return String.valueOf(arr);
    }