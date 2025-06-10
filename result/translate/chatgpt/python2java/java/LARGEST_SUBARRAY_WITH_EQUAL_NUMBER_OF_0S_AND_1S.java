static void f_gold(int args[],int size) {
        int sum = 0;
        int maxsize = -1;
        for(int i = 0; i < size - 1; i++) {
            sum = (args[i] == 0) ? -1 : 1;
            for(int j = i + 1; j < size; j++) {
                sum = (args[j] == 0) ? sum + (-1) : sum + 1;
                if(sum == 0 && maxsize < j - i + 1) {
                    maxsize = j - i + 1;
                    int startindex = i;
                }
            }
        }
        if (maxsize == -1) {
            System.out.println("No such subarray");
        } else {
            System.out.print(startindex + " to " + (startindex + maxsize - 1));
        }
    }
