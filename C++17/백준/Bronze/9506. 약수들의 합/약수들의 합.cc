#include <iostream>
#include <vector>

int main(void){
    int n,sum;
    std::vector<int> nvec;
    n = 1000;
    std::cin >> n;

    while(n > 0){
        sum = 1;
        nvec.clear();
        nvec.push_back(1);
        
        for(int i = 2; i < n; i++){
            if(n % i == 0 && nvec.back() != i){
                if (i == n/i){
                    sum += n/i;
                    nvec.push_back(i);
                }
                else{
                    sum += i;
                    nvec.push_back(i);
                }
            }
            
        }
        
        if(sum == n){
            std::cout << n << " = ";
            int m = nvec.back();
            nvec.pop_back();

            for(const auto& a : nvec){
                std::cout << a << " + ";
            }
            std::cout << m << std::endl;
        }
        else{
            std::cout << n << " is NOT perfect." << std::endl;
        }
        std::cin >> n;
    }
    
    return 0;
}