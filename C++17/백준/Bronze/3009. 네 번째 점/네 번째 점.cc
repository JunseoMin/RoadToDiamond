#include <iostream>
#include <vector>

int main(void){
    int x,y,xres,yres;
    std::vector<int> xs(1001,0);
    std::vector<int> ys(1001,0);
    std::vector<int> px;
    std::vector<int> py;
    
    
    for (int i = 0; i<3; i++){
        std::cin >> x >> y;
        
        px.push_back(x);
        py.push_back(y);
        
        xs[x] += 1;
        ys[y] += 1;
    }
    
    for (const auto& ix : px){
        if (xs[ix] == 1){
            xres = ix;
            continue;
        }
    }
    for (const auto& iy : py){
        if (ys[iy] == 1){
            yres = iy;
            continue;
        }
    }
    
    std::cout << xres << ' ' << yres;
    
    return 0;
}