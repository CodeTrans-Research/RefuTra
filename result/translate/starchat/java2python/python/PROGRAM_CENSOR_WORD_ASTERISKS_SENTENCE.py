def f_gold(text, word):
        word_list = text.split(" ")
        result = ""
        stars = ""
        for i in range(len(word)):
            stars += "*"
        for i, word_i in enumerate(word_list):
            if word_i == word:
                word_list[i] = stars
        for word_i in word_list:
            result += word_i + " "
        return result