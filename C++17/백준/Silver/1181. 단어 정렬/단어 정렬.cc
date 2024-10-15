#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int main(void){
    int N;
    std::string str;
    std::vector<std::vector<std::string>> invec(20001);
    std::cin >> N;

    for (int i = 0; i < N; i++){
        std::cin >> str;
        invec[str.length()].push_back(str);
    }
    
    for (auto& v : invec){
        if (!v.empty()){
            std::sort(v.begin(),v.end());
            v.erase(std::unique(v.begin(),v.end()),v.end());
            for (const auto&str:v){
                std::cout << str << '\n';
            }
        }
    }
    
    return 0;
}