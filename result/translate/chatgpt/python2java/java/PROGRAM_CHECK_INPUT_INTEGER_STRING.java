public boolean f_gold(String s) {
    for (int i = 0; i < s.length(); i++) {
        if (!Character.isDigit(s.charAt(i))) {
            return false;
        }
    }
    return true;
}