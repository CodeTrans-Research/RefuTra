static int f_gold(String stri, int n) {
        HashMap<Character, Integer> m = new HashMap<>();
        for (int i = 0; i < n; i++) {
            m.put(stri.charAt(i), m.getOrDefault(stri.charAt(i), 0) + 1);
        }
        int res = 0;
        for (int i : m.values()) {
            if (i == 2) {
                res += 1;
            }
        }
        return res;
    }
