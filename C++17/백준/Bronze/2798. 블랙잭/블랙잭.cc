#include <iostream>
#include <vector>

int main(void){
    int N,M,in,min = 10000000;
    int tmp;
    std::cin >> N >> M;
    std::vector<int> cards;
    
    for (int i = 0 ; i < N; i++){
        std::cin >> in;
        cards.push_back(in);
    }
    
    for(int i = 0 ; i < N-2; i ++){
        for (int j = i + 1; j < N-1; j++){
            for (int k = j + 1; k < N; k++){
                tmp = M - (cards[i] + cards[j] + cards[k]);
                if (tmp < 0) {continue;}
                min = std::min(min,tmp);
            }
        }
    }
    
    std::cout << M - min;
    return 0;
}