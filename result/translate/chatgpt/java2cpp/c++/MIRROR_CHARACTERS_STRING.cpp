std::string f_gold(std::string str, int n) {
    std::string reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba";
    int l = str.length();
    std::string answer = "";
    for (int i = 0; i < n; i++) {
        if (i < l) answer = answer + str[i];
    }
    for (int i = n; i < l; i++) {
        answer = answer + reverseAlphabet[str[i] - 'a'];
    }
    return answer;
}