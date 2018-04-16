public class LonelyInetgerXOR {
    public static void main(String[] args) {
        int[] arr = {1,1,2,2,3,3,4,4,5,5,212,3232,212};
        int result = 0;
        for(int value :arr){
            result ^= value;
        }//for
        System.out.println(result);
    }//main
}
