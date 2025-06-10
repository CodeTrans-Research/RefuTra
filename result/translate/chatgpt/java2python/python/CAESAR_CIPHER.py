def f_gold(text, s):
    result = ""
    for i in range(len(text)):
        if text[i].isupper():
            ch = chr(((ord(text[i]) + s - 65) % 26) + 65)
            result += ch
        else:
            ch = chr(((ord(text[i]) + s - 97) % 26) + 97)
            result += ch
    return result