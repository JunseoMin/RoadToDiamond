#include <iostream>
#include <string>

int main(void){
    unsigned long long int des = 0;
    unsigned long long int ans = 1;
    std::cin >> des;
    
    if (des == 1){
        std::cout << '1';
        return 0;
    }
    
    int n_next, n_prev;
    n_prev = 1;
    n_next = 7;
    
    while (!(n_prev < des && des <= n_next)){
        n_prev = n_next;
        n_next = n_prev + 6 * (ans + 1);
        ans += 1;
    }
    
    std::cout << ans + 1;
    
    return 0;
}
