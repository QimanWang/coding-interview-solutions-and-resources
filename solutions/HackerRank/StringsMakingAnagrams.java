import java.util.*;
public class StringsMakingAnagrams {
    public static int numberNeeded(String first, String second) {
        HashMap<Character,Integer> fMap = new HashMap();

        int toBeRemoved = 0;
        //first time
        for(int i = 0; i < first.length(); i ++){
            if(fMap.containsKey(first.charAt(i))){
                fMap.replace(first.charAt(i),fMap.get(first.charAt(i))+1);
            }else {
                fMap.put(first.charAt(i),1);
            }//else
        }//fori
        for( HashMap.Entry<Character, Integer> entry : fMap.entrySet()){
            Character key = entry.getKey();
            Integer value = entry.getValue();
            System.out.print(key+""+value+" " );
        }
        System.out.println();
        //second time
        for(int j = 0; j < second.length(); j++){
            if(fMap.containsKey(second.charAt(j))){
                fMap.replace(second.charAt(j),fMap.get(second.charAt(j))-1);
            }else {
                fMap.put(second.charAt(j),-1);
            }//else
        }//forj
        for( HashMap.Entry<Character, Integer> entry : fMap.entrySet()){
            Character key = entry.getKey();
            Integer value = entry.getValue();
            System.out.print(key+""+value+" ");
        }
        System.out.println();
        //calculate the difference
        for(Integer value: fMap.values()){
            toBeRemoved+=Math.abs(value);
            //System.out.println(value);
        }//cout


    return(toBeRemoved);
    }
    public static void main(String args[]){
        //a
        String a = "fcrxzwscanmligyxyvym";
        char[] charsA = a.toCharArray();
        Arrays.sort(charsA);
        String sortedA = new String(charsA);
        System.out.println(sortedA);
        //b
        String b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke";
        char[] charsB = b.toCharArray();
        Arrays.sort(charsB);
        String sortedB = new String(charsB);
        System.out.println(sortedB);

        //System.out.println(numberNeeded("aa","b"));
        System.out.println(numberNeeded("fcrxzwscanmligyxyvym","jxwtrhvujlmrpdoqbisbwhmgpmeoke"));
    }//main
}//class

