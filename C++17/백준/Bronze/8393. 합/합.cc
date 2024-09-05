#include <iostream>

int main(void){
    int n,sum;
    std::cin >> n;
    
    sum = 0;
    for(int i = 1 ; i < n+1; i ++){
        sum += i;
    }
    std::cout << sum;
    return 0;
}