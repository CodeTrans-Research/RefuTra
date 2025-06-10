public static String f_gold(String Str) {
    int Len = Str.length();
    char[] res = new char[Len];
    int index = 0;
    int i = 0;
    Stack<Integer> s = new Stack<Integer>();
    s.push(0);
    while (i < Len) {
        if (Str.charAt(i) == '+') {
            if (s.peek() == 1) {
                res[index] = '-';
                index++;
            }
            if (s.peek() == 0) {
                res[index] = '+';
                index++;
            }
        } else if (Str.charAt(i) == '-') {
            if (s.peek() == 1) {
                res[index] = '+';
                index++;
            } else if (s.peek() == 0) {
                res[index] = '-';
                index++;
            }
        } else if (Str.charAt(i) == '(' && i > 0) {
            if (Str.charAt(i - 1) == '-') {
                int x = (s.peek() == 1) ? 0 : 1;
                s.push(x);
            } else if (Str.charAt(i - 1) == '+') {
                s.push(s.peek());
            }
        } else if (Str.charAt(i) == ')') {
            s.pop();
        } else {
            res[index] = Str.charAt(i);
            index++;
        }
        i++;
    }
    return new String(res);
}