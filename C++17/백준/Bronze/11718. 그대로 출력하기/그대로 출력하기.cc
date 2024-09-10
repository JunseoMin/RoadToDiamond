#include <iostream>

int main(void){
    std::string instr;
    
    while(std::getline(std::cin, instr)){
        std::cout << instr << std::endl;
    }
    
    return 0;
}