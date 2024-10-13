#include <iostream>
#include <vector>
#include <algorithm>

int main(void){
    int N,k,x;
    int j = 0;
    std::vector<int> vec;
    
    std::cin >> N >> k;
    for(int i = 0; i < N; i ++){
        std::cin >> x;
        vec.push_back(x);
    }
    
    std::sort(vec.begin(),vec.end(),std::greater<int>());

    std::cout << vec[k-1];
    
    return 0;
}