#include <vector>
#include <iostream>

int main(void){
    int N;
    std::cin >> N;
    std::vector<std::vector<int>> paper(100,std::vector<int>(100,0));
    
    for (int i=0; i< N; i++){
        int x,y;
        std::cin >> x >> y;
        
        for ( int _x = x; _x < x+10; _x++){
            for (int _y = y; _y < y+10; _y ++){
                paper[_x][_y] = 1;
            }
        }
    }
    int res = 0;
    
    for (const auto& l:paper){
        for(const auto& v:l){
            res += v;
        }
    }
    
    std::cout << res;
    return 0;
}