#include <iostream>

int main(void){
    int a,b,c;
    
    std::cin >> a >> b >> c;
    
    while(a + b + c > 0){
        int sum = a+b+c;
        
        if (a == b && b == c){
            std::cout << "Equilateral" << std::endl;
        }
        else if (sum <= 2 * std::max(std::max(a,b),c)){
            std::cout << "Invalid" << std::endl;
        }
        else if (a != b && b != c && a != c){
            std::cout << "Scalene" << std::endl;
        }
        else{
            std::cout << "Isosceles" << std::endl;
        }
        
        std::cin >> a >> b >> c;
    }
    
    return 0;
}