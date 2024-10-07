#include <iostream>
#include <vector>
#include <string>

std::vector<int> sum(std::vector<int> v1,std::vector<int> v2,int size){
    std::vector<int> res;
    
    for(int i = 0; i < size; i++){
        res.push_back(v1[i] + v2[i]);
    }
    
    return res;
}

int main(void){
    int N,M;
    std::cin >> N >> M;
    
    std::vector<std::vector<int>> mat1;
    
    std::string input;
    std::vector<int> invec;
    
    for(int i = 0; i < 2*N; i++){
        invec.clear();
        input.clear();
        
        for (int j = 0; j<M; j++){
            int value;
            std::cin >> value;
            invec.push_back(static_cast<int>(value));
        }    
        if (i < N) {mat1.push_back(invec);}
        if (i >= N) {mat1[i-N] = sum(mat1[i-N],invec,M);}
    }
    
    for (const auto& l:mat1){
        for (const auto& v:l){
          std::cout << v << " ";
        }
       std::cout << std::endl;
    }
    
    return 0;
}