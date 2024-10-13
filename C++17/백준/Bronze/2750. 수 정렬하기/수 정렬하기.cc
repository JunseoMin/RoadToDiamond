#include <iostream>
#include <vector>

int main(void){
    int N,n;
    std::cin >> N;
    
    std::vector<int> invec;
    std::vector<int> p_sortedvec(1001,-1);
    std::vector<int> n_sortedvec(1001,-1);
    
    for (int i = 0; i < N; i++){
        std::cin >> n;
        invec.push_back(n);
    }
    
    for (int i = 0; i < N; i++){
        if(invec[i] >= 0){
            p_sortedvec[invec[i]] = 1;
        }
        else{
            n_sortedvec[ -1 * invec[i]] = 1;
        }
    }

    for(int i = 1000; i > 0; i--){
        if(n_sortedvec[i] == 1){
            std::cout << -1*i << std::endl;
        }
    }

    for(int i = 0; i < 1001; i++){
        if(p_sortedvec[i] == 1){
            std::cout << i << std::endl;
        }
    }

    return 0;
}