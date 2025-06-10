int f_gold ( string str ) {
    int sum = 0, len = str. length ( );
    for ( int i = 0 ; i < len ; i++ ) {
        char ch = str [ i ];
        if ( isdigit ( ch ) ) {
            string temp = to_string ( ch );
            while ( i + 1 < len && isdigit ( str [ i + 1 ] ) ) temp += str [ i + 1 ], i++;
            sum += stoi ( temp );
        }
    }
    return sum;
}