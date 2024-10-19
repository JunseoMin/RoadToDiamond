#include <iostream>
#include <set>

long long divide(long long A, long long B) {
    if (A % B == 0)
        return B;
    else
        return divide(B, A % B);
}

int main(void){
    int T,a,b,tmp;
    
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);
    
    std::cin >> T;
    
    for (int i = 0; i < T; i ++){
        std::cin >> a >> b;
        
        if ( a > b){
            tmp = divide(a,b);
        }
        else{tmp = divide(b,a);}
        std::cout << a*b / tmp << '\n';
    }
    
    
    return 0;
}