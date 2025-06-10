#include <unordered_map>

int f_gold(int A[], int B[], int n) {
    std::unordered_map<int, int> hash;
    for (int i = 0; i < n; i++) {
        if (hash.count(A[i]))
            hash[A[i]] = 1 + hash[A[i]];
        else
            hash[A[i]] = 1;
        
        if (hash.count(B[i]))
            hash[B[i]] = 1 + hash[B[i]];
        else
            hash[B[i]] = 1;
    }
    
    int sum = 0;
    for (auto entry : hash) {
        if (std::stoi(std::to_string(entry.second)) == 1)
            sum += std::stoi(std::to_string(entry.first));
    }
    
    return sum;
}