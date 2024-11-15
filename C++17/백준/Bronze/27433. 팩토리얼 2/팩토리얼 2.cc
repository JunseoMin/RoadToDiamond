#include <iostream>

long long int factorial(int n){
    if (n < 2){return 1;}
    return n * factorial(n-1);
}

int main(void){
    int n;
    std::cin >> n;
    std::cout << factorial(n);
    return 0;    
}