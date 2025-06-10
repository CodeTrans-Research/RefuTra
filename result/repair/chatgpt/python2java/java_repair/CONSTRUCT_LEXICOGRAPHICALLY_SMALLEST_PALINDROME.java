  String f_gold(String string, int l) {
    char[] stringArr = string.toCharArray();
    int i = -1;
    int j = 1;

    while (i < j) {
        i += 1;
        j -= 1;

        if ( string.charAt( i ) == string.charAt( j ) && string.charAt( i ) != '*' ) {
            continue;
        } else if (stringArr[i] == stringArr[j] && stringArr[i] == '*') {
            stringArr[i] = 'a';
            stringArr[j] = 'a';
            continue;
        } else if string.charAt( i ) == '*' {
            stringArr[i] = stringArr[j];
            continue;
        } else if string.charAt( j ) == '*' {
            stringArr[j] = stringArr[i];
            continue;
        }
        System.out.println("Not Possible");
        return "";
    }

    return new String(stringArr);
}
