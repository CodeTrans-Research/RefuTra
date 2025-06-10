public List<Integer> f_gold(int n){
    List<Integer> res = new ArrayList<>();
    res.add(0);
    res.add(1);
    int i = 2;
    while(i < n + 1){
        res.add(Math.max(i,(res.get((int)i/2) + res.get((int)i/3) + res.get((int)i/4) + res.get((int)i/5))));
        i++;
    }
    return res.get(n);
}