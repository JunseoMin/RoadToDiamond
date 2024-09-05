#include <iostream>

int main(void){
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);
    
    int N,a,b;
    std::cin >> N;
    
    for(int i = 0; i < N; i ++){
        std::cin >> a >> b;
        std::cout << a + b << '\n';
    }
    
    return 0;
}