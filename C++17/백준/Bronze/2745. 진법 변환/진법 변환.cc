#include <iostream>
#include <string>
#include <math.h>

int num_convert(const char &str){
    if ('0' <= str && str <= '9'){
        return str - '0';
    }

    return str - 'A' + 10;
}

int main(void){
    std::string N;
    int B,size;
    std::cin >> N >> B;
    unsigned long long int ans = 0;
    
    size = N.length();

    for(int i = 0; i < size; i++){
        ans += std::pow(B,size -1 -i) * num_convert(N[i]);
    }
    
    std::cout << ans;
    return 0;
}