def f_gold(text, word):
    word_list = text.split()
    result = ""
    stars = ""
    for i in range(len(word)):
        stars += '*'
    index = 0
    for i in range(len(word_list)):
        if word_list[i] == word:
            word_list[i] = stars
    for i in word_list:
        result += i + ' '
    return result