#include <iostream>
#include <algorithm>

int gcd(int a, int b) {

    while (b != 0) {
        int tmp = b;
        b = a % b;
        a = tmp;
    }
    return a;

}

int lcm(int a,int b){
    return (a > 0 && b > 0) ? (std::abs(a*b) / gcd(a,b)) : 0;
}

int main() {
    int a, b, c, d, mom, son, gbs, div;
    std::cin >> a >> b;
    std::cin >> c >> d;
    
    gbs = lcm(b, d);
    son = a * (gbs / b)  + c * (gbs / d);
    
    div = gcd(son, gbs);
    son = son / div;
    mom = gbs / div;
        
    std::cout << son << ' ' << mom << std::endl;

    return 0;
}
