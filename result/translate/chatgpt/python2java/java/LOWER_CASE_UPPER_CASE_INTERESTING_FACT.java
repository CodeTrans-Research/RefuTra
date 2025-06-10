public static String f_gold(char[] in_list) {
    for (int i = 0; i < in_list.length; i++) {
        if ('a' <= in_list[i] && in_list[i] <= 'z') {
            in_list[i] = (char) (in_list[i] - 'a' + 'A');
        }
    }
    return new String(in_list);
}