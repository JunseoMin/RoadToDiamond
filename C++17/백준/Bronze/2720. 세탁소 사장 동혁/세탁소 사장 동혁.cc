#include <iostream>
#include <vector>
#include <string>

int main(void){
    int T,C;
    std::cin >> T;
    int q,d,n;
    
    for(int i = 0; i < T; i++){
        C = 0;
        std::cin >> C;
        q = (C - C%25) / 25;
        C %= 25;
        d = (C - C%10) / 10;
        C %= 10;
        n = (C - C%5) / 5;
        C %= 5;
        std::cout << q << ' ' << d << ' ' << n << ' ' << C << std::endl;
    }
    
    return 0;
}