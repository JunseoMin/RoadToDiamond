#include <iostream>
#include <vector>

int main(void){
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int N,n;
    std::vector<int> vec(10001,0);
    
    std::cin >> N;
    for(int i = 0; i < N; i++){
        std::cin >> n;
        vec[n] += 1;
    }
    
    for(int i  = 1; i < 10001; i ++){
        if (vec[i] != 0){        
            for(int j = 0; j < vec[i]; j++){
                std::cout << i << '\n';
            }
        }
    }
    
    return 0;
}