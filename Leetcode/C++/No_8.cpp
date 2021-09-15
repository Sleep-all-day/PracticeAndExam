#include<iostream>
using namespace std;

class Solution{
public:
    int atoi(string s){
        if(s.size() == 0)return 0;
        bool flag = true;
        int res = 0;
        int index = 0;
        while(s[index] == ' ')index ++;
        if(s[index] == '+'){
            flag = true;
            index ++;
        }
        else if (s[index] == '-'){
            flag = false;
            index ++;
        }
        while(index < s.size() && isdigit(s[index])){

            int temp = s[index] - '0';
            if(res > INT_MAX/10 || (res == INT_MAX/10 && temp > 7)){
                return flag == true ? INT_MAX: INT_MIN;
            }
            res = res * 10 + temp;
            index ++;
        }
        return flag == true ? res: -res;
    }


};

int main(){
    string s = "-91283472332";
    Solution so = Solution();
    int res = so.atoi(s);
    cout << res << endl;
}