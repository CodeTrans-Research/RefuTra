int f_gold(string n) {
    int len = n.length();
    if (len == 1) {
        int oneDigit = n[0] - '0';
        if (oneDigit % 4 == 0) return 1;
        return 0;
    }
    int twoDigit, count = 0;
    for (int i = 0; i < (len - 1); i++) {
        twoDigit = (n[i] - '0') * 10 + (n[i + 1] - '0');
        if (twoDigit % 4 == 0) count++;
    }
    twoDigit = (n[len - 1] - '0') * 10 + (n[0] - '0');
    if (twoDigit % 4 == 0) count++;
    return count;
}