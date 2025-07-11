bool f_gold ( string s ) {
        stack<char> st;
        for (auto &c : s) {
            if (c == ')') {
                if (st.empty() || st.top()!= '(') return false;
                st.pop();
            } else {
                st.push(c);
            }
        }
        return st.empty();
    }