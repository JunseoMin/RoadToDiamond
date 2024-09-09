#include <iostream>

int main(void){
    int a,b;
    while(1){
        std::cin >> a >> b;
        if (std::cin.eof()){
            return 0;
        }
        std::cout << a+b << std::endl;
    }
    return 1;    
}