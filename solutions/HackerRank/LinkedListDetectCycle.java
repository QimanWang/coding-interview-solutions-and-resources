
public class LinkedListDetectCycle {

    boolean hasCycle(Node head) {
        //using floyd's cycle detection method

        Node fast = head;
        Node slow = head;

        while (fast != null && fast.next != null){
            slow = slow.next; //slow moves one node next
            fast = fast.next.next; // fast moves two node next

            //if there is a cycle, the slow and fast will land on the same node at some point
            if(slow == fast){
                return true;
            }
        }
        //if the nodes never met and the list has been iterated through, then there is no cycle.
        return false;
    }

    public static void main(String args[]){

    }//main
}//class
