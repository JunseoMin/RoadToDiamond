#include <iostream>

long long int combination(int n, int r){    
    long long int res = 1;
    r = (n - r > r) ? n - r : r;
    for (int i = 0; i < r; i++){
        res *= (n - i);
        res /= (i + 1);
    }
    return res;
}

int main(void){
    int N, n, r;
    std::cin >> N;
    
    for (int i = 0; i < N; i++){
        std::cin >> r >> n;
        std::cout << combination(n, r) << '\n';
    }
    
    return 0;
}
