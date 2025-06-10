public static int f_gold(String str1){
    int result = 0;
    int n = str1.length();
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(Math.abs(str1.charAt(i) - str1.charAt(j)) == Math.abs(i - j)){
                result += 1;
            }
        }
    }
    return result;
}