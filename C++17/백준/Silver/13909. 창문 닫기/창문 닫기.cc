#include <iostream>
#include <cmath>

int main(void){
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);
    
    int N,res = 1;
    std::cin >> N;
    std::cout << static_cast<int>(std::sqrt(N));
    
    return 0;
}