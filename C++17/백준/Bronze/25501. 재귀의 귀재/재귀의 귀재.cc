#include <iostream>
#include <string>
#include <string.h>

int recursion(const std::string* s, int l, int r, int* iter){
  (*iter)++;
  if(l >= r) return 1;
  else if((*s)[l] != (*s)[r]) return 0;
  else return recursion(s, l+1, r-1, iter);
}

int isPalindrome(std::string* s, int* iter){
  return recursion(s, 0, (*s).size()-1, iter);
}

int main(void){
  std::cin.sync_with_stdio(0);
  std::cin.tie(0);
  std::cout.tie(0);

  std::string instr;
  int T;

  std::cin >> T;


  for (int i = 0; i < T; i++){
    std::cin >> instr;
    int iter = 0;
    std::cout << isPalindrome(&instr,&iter) << ' ' << iter << '\n';
  }

  return 0;
}