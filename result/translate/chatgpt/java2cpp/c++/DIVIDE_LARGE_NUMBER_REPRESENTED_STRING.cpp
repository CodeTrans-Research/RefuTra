std::string f_gold(std::string number, int divisor) {
    std::string ans = "";
    int idx = 0;
    const char *num = number.c_str();
    int temp = num[idx] - '0';
    while (temp < divisor) temp = temp * 10 + (num[++idx] - '0');
    while (strlen(num) > idx) {
        ans += (temp / divisor);
        temp = (temp % divisor) * 10 + num[++idx] - '0';
    }
    if (ans.length() == 0) return "0";
    return ans;
}