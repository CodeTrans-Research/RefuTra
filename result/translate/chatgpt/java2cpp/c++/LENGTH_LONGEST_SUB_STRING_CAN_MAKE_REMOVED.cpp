#include <vector>
#include <utility>
#include <algorithm>

int f_gold(std::string str) {
    std::vector<std::pair<char, int>> arr;
    arr.push_back(std::make_pair('@', -1));
    int maxlen = 0;
    for (int i = 0; i < str.length(); ++i) {
        arr.push_back(std::make_pair(str.at(i), i));
        while (arr.size() >= 3 && arr[arr.size() - 3].first == '1' && arr[arr.size() - 2].first == '0' && arr[arr.size() - 1].first == '0') {
            arr.erase(arr.end()-3, arr.end());
        }
        int tmp = arr[arr.size() - 1].second;
        maxlen = std::max(maxlen, i - tmp);
    }
    return maxlen;
}