string f_gold ( string str ) {
    stack < int > st;
    for ( int i = 0; i < str. length(); i++ ) {
        if ( str[i] == '[' ) {
            st.push( i );
        }
        else if ( str[i] == ']' ) {
            int start = st.top();
            st.pop();
            int len = i - start + 1;
            string temp = str.substr( start + 1, len - 2 );
            int count = 1;
            if (!st.empty()) {
                count = st.top();
                st.pop();
            }
            for ( int j = 0; j < count; j++ ) {
                str.replace( start, start + len, temp );
            }
        }
        else if ( isdigit( str[i] ) ) {
            int num = 0;
            while ( i < str.length() && isdigit( str[i] ) ) {
                num = num * 10 + str[i] - '0';
                i++;
            }
            st.push( num );
        }
    }
    return str;
}