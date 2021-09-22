#include<iostream>
#include<math.h>
using namespace std;

class Solution {
public:
    int divide(int a, int b) {
    if (a == INT_MIN && b == -1) return INT_MAX;

    bool sign = (a > 0) ^ (b > 0) ? false : true;

    unsigned int ua = abs(a);
    unsigned int ub = abs(b);
    unsigned int res = 0;
    for (int i = 31; i >= 0; i--) {
        if ((ua >> i) >= ub) {
            ua = ua - (ub << i);
            res += 1 << i;
        }
    }
    // bug 修复：因为不能使用乘号，所以将乘号换成三目运算符
    return sign == true ? res : -res;
}

};

int main()
{
    Solution s = Solution();
    int a = 20;
    int b = 3;
    cout<< s.divide(a, b) << endl;
    return 0;
}
