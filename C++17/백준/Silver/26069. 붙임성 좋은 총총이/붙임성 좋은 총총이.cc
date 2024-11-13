#include <iostream>    
#include <map>
#include <string>

int main(void){
    std::map<std::string,bool> cc;    
    int N;
    std::string p1,p2;
    std::cin >> N;
    
    cc["ChongChong"] = true;
    
    for(int i = 0; i < N ; i ++){
        std::cin>>p1;
        std::cin>>p2;      
        
        if(cc[p1] || cc[p2]){
            cc[p2] = true;
            cc[p1] = true;
        }
        
        if (!cc[p1] || !cc[p2])
        {
            cc.erase(p1);
            cc.erase(p2);
        }
        
    }

    std::cout << cc.size();
    return 0;
}