public static String f_gold ( String text, String word ) {
        String[] word_list = text.split(" ");
        String result = "";
        int stars = word.length();
        for (int i = 0; i < word_list.length; i++) {
            if (word_list[i].equals(word)) {
                result = result + ("*" + word + "*");
            } else {
                result = result + word_list[i] + " ";
            }
        }
        return result;
    }