string f_gold ( string text, int s ) {
        string result = "";
        for ( int i = 0; i < text.length(); i++ ) {
            if ( isupper(text[i]) ) {
                char ch = (char)( ( (int)text[i] + s - 'A' + 1 ) % 26 + 'A' );
                result += ch;
            }
            else {
                char ch = (char)( ( (int)text[i] + s - 'a' + 1 ) % 26 + 'a' );
                result += ch;
            }
        }
        return result;
    }