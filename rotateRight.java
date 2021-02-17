public class rotateRight {
    public ListNode rotateRight(ListNode head, int k) {
        int size = 1;
        ListNode current = head;
        ListNode last = head;
        if (head == null) {
            return null;
        }
        while (current.next != null) {
            current = current.next;
            size++;
        }
        //Size is finalized
        int numRotations = k % size;
        last = current;
        last.next = head;
        //1->2->3->4->5->1
        int leftRotations = size - numRotations;
        while (leftRotations > 0) {
            head = head.next;
            current = current.next;
            leftRotations--;
        }
        current.next = null;
        return head;
    }

    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { 
            this.val = val; 
        }
        ListNode(int val, ListNode next) { 
            this.val = val; 
            this.next = next; 
        }
    }
}
