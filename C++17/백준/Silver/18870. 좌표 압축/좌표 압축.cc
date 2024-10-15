#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

int main(void){
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    int N,x;
    std::cin >> N;
    std::vector<int> invec;
    std::vector<int> xvec;
    
    for (int i = 0; i < N; i++){
        std::cin >> x;
        invec.push_back(x);
        xvec.push_back(x);
    }
    std::sort(invec.begin(),invec.end());
    invec.erase(std::unique(invec.begin(),invec.end()),invec.end());
    
    std::map<int,int> nummap;
    
    for(int i = 0; i < invec.size(); i ++){
        nummap.insert(std::make_pair(invec[i],i));
    }
    for(const auto& n : xvec){
        std::cout << nummap[n] << ' ';
    }
    
    return 0;
}