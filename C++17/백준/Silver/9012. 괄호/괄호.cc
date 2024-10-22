#include <iostream>
#include <vector>
#include <string>

void tester(const std::string& instr, std::vector<char>& left_parenthesis){
    left_parenthesis.clear();
    
    for(const auto& p: instr){
        switch((p == '(' ? 0:1)){
                case 0:
                left_parenthesis.push_back(p);
                break;
                case 1:
                if(left_parenthesis.empty()){
                    std::cout << "NO" << '\n';
                    return;
                }
                left_parenthesis.pop_back();
            }
    }

    if(!left_parenthesis.empty()){
        std::cout << "NO" << '\n';
        return;
    }
    else
    {
        std::cout << "YES" << '\n';
        return;
    }
}

int main(void){
    int N;
    std::string instr;
    std::vector<char> left_parenthesis;

    std::cin >> N;
    
    for(int i = 0; i< N; i++){
        std::cin >> instr;
        tester(instr,left_parenthesis);
    }
    
    return 0;
}