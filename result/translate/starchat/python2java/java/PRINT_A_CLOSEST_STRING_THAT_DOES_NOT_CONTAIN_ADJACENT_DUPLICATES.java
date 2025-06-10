public static String f_gold ( String s ) {
        int n = s. length ( );
        for ( int i = 1 ; i < n ; i++ ) {
            if ( s. charAt ( i ) == s. charAt ( i - 1 ) ) {
                s = s. replace ( s. charAt ( i ), 'a' );
                while ( s. charAt ( i ) == s. charAt ( i - 1 ) || ( i + 1 < n && s. charAt ( i ) == s. charAt ( i + 1 ) ) )
                    i++;
            }
        }
        return s;
    }

Explanation:

The idea is to replace all the characters at indices such that they are not equal to their previous character and not equal to the next character. We increment i till we find a character that satisfies the condition.