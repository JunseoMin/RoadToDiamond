#include <iostream>
#include <string>

bool is_in(const std::string& str1,const std::string& str2, const int n){
    std::string tmp;

    for (int i = 0; i < str1.size() - n + 1; i++){
        if (str1.substr(i,n).compare(str2) == 0)
        {
          return true;
        }
    }

    return false;
}

int main(void){
    int N,res = 666,n = 1;
    std::cin >> N;
    while(n != N){
        res += 1;
        if (is_in(std::to_string(res),"666",3)){
            n++;
        }
    }
        
    std::cout << res;
    
    return 0;
}