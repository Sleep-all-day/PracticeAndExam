#include"ListNode.h"
#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
// 24. 两两交换链表中的节点
// 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
// 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

// 示例 1：
// 输入：head = [1,2,3,4]
// 输出：[2,1,4,3]

// 示例 2：
// 输入：head = []
// 输出：[]

// 示例 3：
// 输入：head = [1]
// 输出：[1]


class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
       if(head == nullptr || head->next == nullptr)return head;
       ListNode* newhead = head->next;
       head ->next = swapPairs(newhead->next);
       newhead->next = head;
       return newhead;
    }
};

// int main(){
//     ListNode* head = new ListNode();
//     ListNode* dummy = head;
//     for(int i = 1; i < 9 ;i++){
//         dummy->val = i;
//         dummy -> next = new ListNode();
//         dummy = dummy -> next;
//     }
//     while(head != nullptr){
//         cout << head->val << endl;
//         head = head->next;
//     }

//     Solution s = Solution();
//     ListNode* res = s.swapPairs(head);
//     while(res != nullptr){
//         cout << res->val << endl;
//         res = res->next;
//     }
// }