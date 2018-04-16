import java.util.HashMap;

public class CoinChangeDP {

    //make change
    public static long makeChange(int[] coins, int total, int index, HashMap<String, Long> memo){

        //2 base case
        if(total ==0){
            return 1;
        }//if total hits 0,
        if(index >= coins.length){
            return 0;
        }//if no coin left

        //keep track of current computed and what coins have been used
        String key = total +":"+ index;
        if(memo.containsKey(key)){
            return memo.get(key);
        }//return if already have record of it being already computed

        int currentAmount =0;
        long ways = 0;
        while(currentAmount <= total) {
            int leftOver = total - currentAmount;
            ways += makeChange(coins, leftOver, index+1, memo);
            currentAmount += coins[index];
        }//while not done yet

        //store computed and return
        memo.put(key,ways);
        return ways;
    }//make change

    public static void main(String[] args) {
        int[] coins ={1,2,3,4,5,6,7,8,9,10};
        HashMap<String,Long> memo = new HashMap<>();
        System.out.println(makeChange( coins,10,0,memo));

    }
}
