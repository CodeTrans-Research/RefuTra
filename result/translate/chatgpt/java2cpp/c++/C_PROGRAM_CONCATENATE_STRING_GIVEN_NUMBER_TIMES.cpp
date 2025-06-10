#include <string>

std::string f_gold(std::string s, int n) {
    std::string s1 = s;
    for (int i = 1; i < n; i++) {
        s += s1;
    }
    return s;
}