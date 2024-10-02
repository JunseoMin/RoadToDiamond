#include <iostream>
#include <vector>

int main(void){
    std::vector<int> piece{1,1,2,2,2,8};
    for(int i=0; i < 6; i++){
        int in = 0;
        std::cin >> in;
        std::cout << piece.at(i) - in << std::endl;
    }
    
    return 0;
}