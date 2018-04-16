import java.util.*;

    class MyQueue<Integer> {
    Stack<Integer> inputStack = new Stack<>();
    Stack<Integer> outputStack = new Stack<>();
    public void enqueue(Integer x){
        inputStack.push(x);
    }//enqueue method
    public Integer dequeue(){
        if(outputStack.isEmpty()) {
            while (!inputStack.isEmpty()) {
                outputStack.push(inputStack.pop());
            }//while Input stack has more items, we transfer them to output stack
        }//if output stack is empty
        if(!outputStack.isEmpty()) {
            return outputStack.pop();
        }
        return null;
    }//dequeue method
    public Integer peek(){
        if(outputStack.isEmpty()) {
            while (!inputStack.isEmpty()) {
                outputStack.push(inputStack.pop());
            }//while stackinput has more items, we transfer them to output stack
        }//if output stack is empty
        if(!outputStack.isEmpty()) {
            return outputStack.peek();
        }
        return null;
    }//dequeue method

}//class:myqueue
public class QueueUsingTwoStacks {

    public static void main(String args[]){
        MyQueue<Integer> queue = new MyQueue<Integer>();

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        for (int i = 0; i < n; i++) {
            int operation = scan.nextInt();
            if (operation == 1) { // enqueue
                queue.enqueue(scan.nextInt());
            } else if (operation == 2) { // dequeue
                queue.dequeue();
            } else if (operation == 3) { // print/peek
                System.out.println(queue.peek());
            }
        }
        scan.close();
    }//main
}//class
/* example input
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2
output:
14
14
 */
