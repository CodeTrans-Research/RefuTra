public static String f_gold(String s) {
  if (s.equals(" ")) {
    return "a";
  }
  int i = s.length() - 1;
  while (i >= 0 && s.charAt(i) == 'z') {
    i--;
  }
  if (i == -1) {
    s = s + 'a';
  } else {
    s = s.substring(0, i) + (char)(s.charAt(i) + 1) + s.substring(i + 1);
  }
  return s;
}