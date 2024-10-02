#include <iostream>
#include <vector>

int main(void){
    std::string instr;
    std::cin >> instr;
    int l = instr.length();
       
    for(int i=0; i<l/2 ; i++){
        if (instr.at(i) != instr.at(l - i - 1)){
            std::cout << 0;
            return 0;
        }
    }
    std::cout << 1;
    return 0;
}