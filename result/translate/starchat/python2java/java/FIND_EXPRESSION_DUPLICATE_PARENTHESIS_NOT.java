public static boolean f_gold ( String string ) {
        Stack < Character > Stack = new Stack < > ( );
        for ( int i = 0 ; i < string. length ( ) ; i ++ ) {
            char ch = string. charAt ( i );
            if ( ch == ')' ) {
                char top = Stack. pop ( );
                int elementsInside = 0;
                while ( top!= '(' ) {
                    elementsInside ++;
                    top = Stack. pop ( );
                }
                if ( elementsInside < 1 ) return true;
            } else Stack. push ( ch );
        }
        return false;
    }