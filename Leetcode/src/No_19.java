/*给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]*/

public class No_19 {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode first = dummy;
        ListNode second = dummy;
        for(int i = 0; i < n; i++){
            if(head.next != null) {
                second = second.next;
            }
            else return null;
        }

        while(second.next != null){
            first = first.next;
            second = second.next;
        }

        if(n == 1)first.next = null;
        else first.next = first.next.next;


        return dummy.next;
    }
}
