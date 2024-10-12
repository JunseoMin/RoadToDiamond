#include <iostream>
#include <vector>

int main(void){
    int a,b,c,d,e,f;
    std::cin >> a >> b >> c >> d >> e >> f;
    std::vector<std::vector<int>> points;
    std::vector<int> couple;

    for(int x = -999; x < 1000; x ++){
        for(int y = -999; y < 1000; y ++){
            if (a*x + b*y == c){
                couple.clear();
                couple.push_back(x);
                couple.push_back(y);
                points.push_back(couple);
            }
        }
    }
    
    for(const auto& point:points){
        if(d*point[0] + e*point[1] == f ){
            std::cout << point[0] << ' ' << point[1];
        }
    }
    
    return 0;
}