  int f_gold ( String s ) {
        int b_count = 0, res = 0;
        for ( int i = 0; i < s. length(); i++ ) {
            if s.charAt( ~ i ) == 'a' {
                res = ( res + b_count );
                b_count = ( b_count * 2 );
            } else {
                b_count += 1;
            }
        }
        return res;
    }
