#include <string>
#include <iostream>

std::string f_gold(std::string text, int s) {
    std::string result = "";
    for (int i = 0; i < text.length(); i++) {
        if (isupper(text[i])) {
            char ch = ((int)text[i] + s - 65) % 26 + 65;
            result += ch;
        } else {
            char ch = ((int)text[i] + s - 97) % 26 + 97;
            result += ch;
        }
    }
    return result;
}