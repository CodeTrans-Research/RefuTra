def f_gold ( str ) :
    st = Stack ( )
    for c in str :
        st.push ( c )
    for c in str :
        str = st.pop ( )
        st.push ( c )
    return str