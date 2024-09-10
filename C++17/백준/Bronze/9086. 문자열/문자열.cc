#include <iostream>

int main(void){
    std::string instr;
    int T;
    std::cin >> T;
    
    for(int i = 0; i < T; i++){
        instr.clear();
        std::cin >> instr;
        std::cout << instr[0] << instr.back() << std::endl;
    }
    return 0;
}