#include <iostream>
#include <set>

int main(void){
    int nA,nB,n;
    std::cin >> nA >> nB;
    std::set<int> nums;
    
    for (int i = 0; i < nA + nB; i ++){
        std::cin >> n;
        nums.insert(n);
    }

    std::cout << - nA - nB + 2 * static_cast<int>(nums.size());
    
    return 0;
}