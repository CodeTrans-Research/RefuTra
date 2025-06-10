public static String f_gold(String string, int l) {
    char[] stringArr = string.toCharArray();
    int i = -1;
    int j = 1;

    while (i < j) {
        i += 1;
        j -= 1;

        if (stringArr[i] == stringArr[j] && stringArr[i] != '*') {
            continue;
        } else if (stringArr[i] == stringArr[j] && stringArr[i] == '*') {
            stringArr[i] = 'a';
            stringArr[j] = 'a';
            continue;
        } else if (stringArr[i] == '*') {
            stringArr[i] = stringArr[j];
            continue;
        } else if (stringArr[j] == '*') {
            stringArr[j] = stringArr[i];
            continue;
        }
        System.out.println("Not Possible");
        return "";
    }

    return new String(stringArr);
}