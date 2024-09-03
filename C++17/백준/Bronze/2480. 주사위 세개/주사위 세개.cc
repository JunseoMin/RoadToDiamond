#include <iostream>

int main(void){
    int a,b,c;
    std::cin >> a >> b >> c;
    
    if (a == b && b == c){
        std::cout << 10000 + a * 1000;
        return 0;
    }
    
    if ( a == b || a == c){
        std::cout << 1000 + a*100;
        return 0;
    }
    else if (b == c){
        std::cout << 1000 + b * 100;
        return 0;
    }
    
    std::cout << std::max(std::max(a,b),c) * 100;
    return 0;
}