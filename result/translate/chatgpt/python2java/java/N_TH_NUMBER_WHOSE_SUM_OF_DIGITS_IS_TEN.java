public int f_gold(int n) {
    int count = 0;
    Iterator<Integer> iterator = new Iterator<Integer>() {
        int curr = 0;
        
        @Override
        public boolean hasNext() {
            return true;
        }

        @Override
        public Integer next() {
            int x = curr;
            int sum = 0;
            while (x > 0) {
                sum += x % 10;
                x /= 10;
            }
            if (sum == 10) {
                count++;
            }
            if (count == n) {
                return curr++;
            }
            return curr++;
        }
    };
  
    return -1;
}