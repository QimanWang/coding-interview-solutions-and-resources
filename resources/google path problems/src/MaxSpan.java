import java.util.HashMap;

public class MaxSpan {

    static int maxSpan(int[] nums){
        HashMap<Integer, int[]> hm = new HashMap<>();
        for(int i=0; i < nums.length; i++){
            if(hm.containsKey(nums[i])){
                hm.get(nums[i])[1] = i;
            }//if key already exists
            else{
                int[] idxArr = new int[2];
                idxArr[0]=i;
                hm.put(nums[i],idxArr);
            }
        }
        int max =0;
        for(Object o : hm.keySet()){
            //System.out.println(o);
            int diff = hm.get(o)[1] - hm.get(o)[0]+1;
            if (diff >max) max = diff;

        }
        return max;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,1,1,3};
        int[] nums2= {1, 4, 2, 1, 4, 4, 4};
        System.out.println("{1,2,1,1,3}: " + maxSpan(nums));
        System.out.println("{1, 4, 2, 1, 4, 4, 4}: "+maxSpan(nums2));
    }
}
