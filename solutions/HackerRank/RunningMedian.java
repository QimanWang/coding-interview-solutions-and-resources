import java.io.*;
import java.util.*;
public class RunningMedian {
    /* we use this approach is we want to modularize the code.
    modularize the code will help you identify where things go wrong because you
    make functions to do things. but it does take more time.
    so if you are doing good and wants to save time, don;t use modular.

    public static void addToHeap(int num,PriorityQueue<Integer> lowers, PriorityQueue<Integer> uppers){
        if(!lowers.isEmpty() && num <= lowers.peek()){
            lowers.offer(num);
        }// when element can not be added to collection the add method throws an exception and offer doesn't.
        //we always keep the upper heap bigger by 1 when first insert
        else{
            uppers.offer(num);
        }
    }//addToHeap

    public static void reBalance(PriorityQueue<Integer> lowers, PriorityQueue<Integer> uppers){
        while(lowers.size() > uppers.size()){
            uppers.offer(lowers.poll());
        }//if lower has more
        while(uppers.size() - lowers.size() > 1){
            lowers.offer(uppers.poll());
        }//if upper has 2 or more, we give priority value to min,
        //this guarantees upper to always have 1 more than lower when unbalanced
    }//rebalance

    public static double findMedian(PriorityQueue<Integer> lowers, PriorityQueue<Integer> uppers){
        double median;
        if(lowers.size() == uppers.size()){
            median = (lowers.peek()+uppers.peek())/2.0;
        }//if lower and upper have same size
        else{
            median = uppers.poll();
        }//not balanced, so upper has 1 more, return upper priority value
        return median;
    }//findMedian
*/
    public static void main(String args[]){

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];

        //default priority key is min value
        PriorityQueue<Integer> lowers = new PriorityQueue<Integer>(Comparator.reverseOrder()); //max num is priority
        PriorityQueue<Integer> uppers = new PriorityQueue<Integer>(); //min num is priority

        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
            int num = a[a_i];
            if(!lowers.isEmpty()&& num <=lowers.peek()){
                lowers.offer(num);
            }//if lower is not empty and num is smaller than lower priority value.
            //if lower is empty we want to put it in upper because we want to make sure upper is
            //always equal to lower or 1 size bigger than lower
            else{
                uppers.offer(num);
            }//add to upper if lower is empty, which means it's the first value
             //or the value is not smaller than lower priority value

            //rebalance time
            while(lowers.size() > uppers.size()){
                uppers.offer(lowers.poll());
            }// while the lower heap has more element, we give the priority value to upper.
            while(uppers.size() - lowers.size() >1 ){
                lowers.offer(uppers.poll());
            }//as long as upper don't have 2 or more element than lower, we are gucci

            //find medium
            double medium =0.0;
            if(lowers.size()==uppers.size()){
                medium = (lowers.peek()+uppers.peek())/2.0;
            }// if size is equal, that means we take the two priority , add them and divide by 2.
            else{
                medium = uppers.peek();
            }// if size is not equal, that means upper has 1 more element, so we return upper
            System.out.println(medium);

        /*if you wanted to modular the code
        addToHeap(num, lowers,uppers);
        reBalance(lowers,uppers);
        System.out.println(findMedian(lowers,uppers));
        */
        }//for
    }//main

}//class
