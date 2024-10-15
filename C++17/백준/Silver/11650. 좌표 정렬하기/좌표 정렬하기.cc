#include <iostream>
#include <algorithm>
#include <vector>

int main(void){
    int N;
    
    std::cin >> N;
    std::vector<std::pair<int,int>> invec;
    std::pair<int,int> pair;
    
    for (int i= 0; i<N; i++){
        std::pair<int,int> pair;
        std::cin >> pair.first >> pair.second;
        invec.push_back(pair);
    }
    
    std::sort(invec.begin(),invec.end());
    
    for (const auto& p : invec){
        std::cout << p.first << ' ' << p.second << '\n';
    }

    return 0;
}