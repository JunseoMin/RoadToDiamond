#include <iostream>
#include <vector>

int main(void){
    int N,x,curr=1;
    std::vector<int> waitingline;
    std::cin >> N;
    
    
    for (int i = 0; i< N; i++){
        std::cin >> x;
        if (x == curr)
        {
            curr ++;
            while ((!waitingline.empty()) && waitingline.back() == curr)
            {
                waitingline.pop_back();
                curr ++;
            }
        }
        else{
            waitingline.push_back(x);
        }
        
    }

    if(waitingline.empty()){
        std::cout << "Nice";
    }
    else{
        std::cout << "Sad";
    }
    
    return 0;
}

/*
6
6 4 2 1 3 5
*/