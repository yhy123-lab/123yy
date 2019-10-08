## 添加哨兵加快慢指针

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        if (head == null){
            return null;
        }
        ListNode sentinel = new ListNode(0);
        sentinel.next = head;
        ListNode slow = sentinel;
        ListNode fast = sentinel;
        while (fast != null){
            if (fast.next == null){
                slow = slow.next;
                break;
            }
            else{
                slow = slow.next;
                fast = fast.next.next;
            }
        }
        return slow;
    }
}
