#include <iostream>
int main(void){
    int x,y;
    char tmp;
    std::cin >> x >> y;
    
    if (x > 0 && y > 0){
        std::cout << '1';
        return 0;
    }
    if (x<0 && y<0){
        std::cout << '3';
        return 0;
    }
    if (x>0 && y<0){
        std::cout << '4';
        return 0;
    }
    std::cout << '2';
    return 0;
}