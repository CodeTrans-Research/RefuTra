public static String f_gold(String text, String word) {
    String[] wordList = text.split(" ");
    String result = "";
    String stars = "*".repeat(word.length());
    int count = 0;
    int index = 0;
    for (int i = 0; i < wordList.length; i++) {
        if (wordList[i].equals(word)) {
            wordList[index] = stars;
        }
        index++;
    }
    result = String.join(" ", wordList);
    return result;
}