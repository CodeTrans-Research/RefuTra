#include <string>
#include <algorithm>

std::string f_gold(std::string str) {
    int n = str.length();
    std::string arr[n];
    std::string concat = str + str;
    for (int i = 0; i < n; i++) {
        arr[i] = concat.substr(i, n);
    }
    std::sort(arr, arr + n);
    return arr[0];
}