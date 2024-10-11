#include <iostream>

int main(void){
    int N,x,y;
    std::cin >> N;
    
    int minx = 10000 ,miny = 10000 ,maxx = -10000 ,maxy = -10000;
    
    for (int i = 0; i<N; i++){
        std::cin >> x >> y;
        
        minx = std::min(minx, x);
        miny = std::min(miny, y);
        maxx = std::max(maxx, x);
        maxy = std::max(maxy, y);
    }
    
    if (minx == maxx && maxy == miny){
        std::cout << 0;
        return 0;
    }

    std::cout << std::abs(maxx - minx) * std::abs(maxy - miny);
    
    return 0;
}