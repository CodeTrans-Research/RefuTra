public static char f_gold(String strA, String strB) {
    int res = 0;
    for (int i = 0; i < strA.length(); i++) {
        res = res ^ (int) (strA.charAt(i));
    }
    
    for (int i = 0; i < strB.length(); i++) {
        res = res ^ (int) (strB.charAt(i));
    }
    
    return ((char)(res));
}