#include <iostream>
#include <vector>

int main(void){
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);
    
    int N,com,x;
    std::cin >> N;
    std::vector<int> stack;

    for(int i=0; i< N; i++){
        std::cin >> com;
        switch(com){
            case 1:
                std::cin >> x;
                stack.push_back(x);
                break;
            case 2:
                if (!stack.empty()) {
                    std::cout << stack.back() << '\n';
                    stack.pop_back();
                } else {
                    std::cout << -1 << '\n';
                }
                break;
            case 3:
                std::cout << stack.size() << '\n';
                break;
            case 4:
                std::cout << (stack.empty() ? 1 : 0) << '\n';  // print -1 if empty
                break;
            case 5:
                std::cout << (stack.empty() ? -1 : stack.back()) << '\n';
                break;
        }
    }
    
    return 0;
}