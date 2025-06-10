public boolean f_gold(String isbn) {
    if (isbn.length() != 10) {
        return false;
    }
    int _sum = 0;
    for (int i = 0; i < 9; i++) {
        if (0 <= Integer.parseInt(isbn.charAt(i)) <= 9) {
            _sum += Integer.parseInt(isbn.charAt(i)) * (10 - i);
        } else {
            return false;
        }
    }
    if (isbn.charAt(9) != 'X' && 0 <= Integer.parseInt(isbn.charAt(9)) <= 9) {
        return false;
    }
    _sum += 10 if isbn.charAt(9) == 'X' else Integer.parseInt(isbn.charAt(9));
    return (_sum % 11 == 0);
}