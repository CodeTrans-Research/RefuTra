string f_gold ( string number, int divisor ) {
        string ans = "";
        int idx = 0;
        char num[number.length()];
        for (int i = 0; i < number.length(); i++)
            num[i] = number[i];
        int temp = num[idx] - '0';
        while (temp < divisor) temp = temp * 10 + (num[idx++] - '0');
        while (idx < number.length()) {
            ans += to_string((temp / divisor));
            temp = (temp % divisor) * 10 + num[idx++] - '0';
        }
        if (ans.length() == 0) return "0";
        return ans;
    }