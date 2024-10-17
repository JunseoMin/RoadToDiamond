#include <iostream>
#include <map>
#include <vector>

int main(void){
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);
    
    std::map<int,int> map;
    std::vector<int> nvec;
    
    int N,M,x;
    std::cin >> N;
    for (int i = 0; i < N; i++){
        std::cin >> x;
        map[x] += 1;
    }

    std::cin >> M;
    for(int i=0; i<M; i++){
        std::cin >> x;
        std::cout << map[x] << ' ';
    }
    
    return 0;
}