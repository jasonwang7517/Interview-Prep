/*
    Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either
    0 or 1. The linked list holds the binary representation of a number.

    Return the decimal value of the number in the linked list.
*/
public class ConvertBinaryNumberInALinkedListToInteger {
    class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { 
            this.val = val; 
        }
        ListNode(int val, ListNode next) { 
            this.val = val; this.next = next; 
        }
     }

    public int getDecimalValue(ListNode head) {
        String s = Integer.toString(head.val);
        ListNode n = head;
        while (n.next != null) {
            s += Integer.toString(n.next.val);
            n = n.next;
        }
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(s.length() - i - 1);
            int cInt = Integer.parseInt(String.valueOf(c));
            ans += cInt * Math.pow(2, i);
        }
        return ans;
    }
}
