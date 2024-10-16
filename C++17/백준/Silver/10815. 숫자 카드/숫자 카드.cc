#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

int main(void){
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    int N,M,in;
    std::map<int,int> sanggun;
    std::cin >> N;
    
    for(int i = 0; i< N; i++){
        std::cin >> in;
        sanggun.insert(std::make_pair(in,1));
    }
    
    std::cin >> M;
    for(int i = 0; i< M; i++){
        std::cin >> in;
        std::cout << sanggun[in] << ' ';
    }
    
    return 0;
}