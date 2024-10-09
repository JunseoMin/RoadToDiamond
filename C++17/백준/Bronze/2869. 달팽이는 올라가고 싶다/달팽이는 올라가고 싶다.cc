#include <iostream>

int main(void){
    int A,B,V,d;
    std::cin >> A >> B >> V;
    
    d = A - B;
    
    if ((V - A) % d == 0){
        std::cout << (V - A) / d + 1;
        return 0;
    }
    
    std::cout << (V - A) / d + 2;
    return 0;
}