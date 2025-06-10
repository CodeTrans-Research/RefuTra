def f_gold(str):
    st = []
    for i in range(len(str)):
        st.append(str[i])
    for i in range(len(str)):
        str[i] = st[-1]
        st.pop()
    return ''.join(str)