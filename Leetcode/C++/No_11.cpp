#include<iostream>
#include<vector>
#include<math.h>
using namespace std;

class Solution{
public:
    int maxArea(vector<int>& height){
        int left = 0, right = height.size()-1;
        int res = 0;
        while(left < right){
            int area = min(height[left], height[right]);
            res = max(res, (area * (right - left)));
            if(height[left] < height[right]) left ++;
            else right--;
        }
        return res;
    }
};

// int main(){
//     Solution s = Solution();
//     vector<int> heights;
//     heights.push_back(1);
//     heights.push_back(8);
//     heights.push_back(6);
//     heights.push_back(2);
//     heights.push_back(5);
//     heights.push_back(4);
//     heights.push_back(8);
//     heights.push_back(3);
//     heights.push_back(7);
//     int res = s.maxArea(heights);
//     cout << res << endl;
//     return 0;
// }