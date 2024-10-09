#include <iostream>

int main(void){
    int A,B;
    
    std::cin >> A >> B;
    
    while (A+B){
        
        if (A%B == 0){
            std::cout << "multiple" << std::endl;
            std::cin >> A >> B;
            continue;
        }
        
        if (B%A == 0){
            std::cout << "factor" << std::endl;
            std::cin >> A >> B;
            continue;
        }
        std::cout << "neither" << std::endl;
        std::cin >> A >> B;
    }
    
    return 0;
}