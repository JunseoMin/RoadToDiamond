#include <iostream>
#include <vector>

int main(void){
  std::cin.sync_with_stdio(0);
  std::cout.sync_with_stdio(0);
  std::cin.tie(0);

  int n,m,tmp,a,b,sum = 0;
  std::vector<int> invec;
  std::vector<int> svec;

  std::cin >> n >> m;

  for(int i = 0; i < n; i++){
    std::cin >> tmp;
    invec.push_back(tmp);
  }

  for(const auto& v : invec){
    svec.push_back(sum);
    sum += v;
  }
  svec.push_back(sum);


  for (int i = 0; i < m; i++){
    std::cin >> a >> b;
    std::cout << svec[b] - svec[a-1] << '\n';
  }

  return 0;
}