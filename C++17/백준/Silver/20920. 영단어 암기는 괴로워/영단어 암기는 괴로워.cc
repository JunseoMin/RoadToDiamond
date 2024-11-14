#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

int main() {
    std::map<std::string, int> dic;
    int N, M;
    std::cin >> N >> M;
    std::string word;
    
    for (int i = 0; i < N; i++) {
        std::cin >> word;
        if (word.size() >= M) {
            dic[word]++;
        }
    }

    std::vector<std::pair<std::string, int>> words(dic.begin(), dic.end());

    std::sort(words.begin(), words.end(), [](const auto& a, const auto& b) {
        if (a.second != b.second)
            return a.second > b.second; 
        if (a.first.size() != b.first.size())
            return a.first.size() > b.first.size(); 
        return a.first < b.first;
    });

    for (const auto& ans : words) {
        std::cout << ans.first << '\n';
    }
    return 0;
}
