#include <iostream>
#include <cmath>

bool is_sosu(long long int n){
    if (n == 0 || n == 1){
        return false;
    }

    for (int i = 2; i < static_cast<int>(std::sqrt(n)) + 1; i ++){
        if (n%i == 0){
            return false;
        }
    }
    return true;
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);
    int T;
    long long int n;  
    std::cin >> T;

    for (int i = 0; i < T; ++i) {
        std::cin >> n;

        while (!is_sosu(n)) {
            n++;
        }
        std::cout << n << '\n';
    }

    return 0;
}
