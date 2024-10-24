#include <iostream>

int factorial(int n) {
    int res=1;
    for (int k = n; k > 0; k--)
        res *= k;
    return res;
}

int main(void){
    int N;
    std::cin >> N;
    std::cout << factorial(N);
    return 0;
}