#include <iostream>
#include <vector>

int main(void){
    int M,N,sum,small;
    small = 1000000;
    sum = 0;
    std::vector<int> nums;

    std::cin >> M;
    std::cin >> N;
    
    if (N == 1)
    {
        std::cout << "-1";
        return 0;
    }

    for(int i = 0; i < N+1; i++){
        nums.push_back(i);
    }
    nums[1] = 0;

    for(int n = 1; n < N+1; n ++){
        if (nums[n] != 0){
            for(int i = 2; i*n < N+1; i++){
                nums[i*n] = 0;
            }
        }
    }
    
    for(int i = M; i < N+1; i++){
        if (nums[i] != 0){
            small = std::min(nums[i],small);
            sum += nums[i];
        }
    }
    
    if(sum == 0){
        std::cout << "-1";
        return 0;
    }
    
    std::cout << sum << std::endl;
    std::cout << small;
    
    return 0;
}