#include <iostream>
#include <vector>
#include <algorithm>

int main(void){
    int n,tmp;
    std::cin >> n;
    std::vector<int> yaksus;
    
    for(int i=0; i < n; i++){
        std::cin >> tmp;
        yaksus.push_back(tmp);
    }
    
    std::sort(yaksus.begin(),yaksus.end());
    std::cout << (yaksus.size() > 1 ? yaksus.front() * yaksus.back() : yaksus.front() * yaksus.front());
}