import java.util.HashMap;

/**
 * Created by qiman on 1/12/2017.
 */
public class HashTableRansomNote {

    public static void main(String args[]){

        int m = 6;
        int n = 4;
        //String magazine[] = new String["give", me ,one, grand, today, night]; //
        String a = "give me one grand today night";
        String[] magazine = a.split(" ");
        String b = "give one grand today";
        String[] ransom = b.split(" ");

        if(m<n){
            System.out.println("No1");
        }else{
            HashMap<String,Integer> magazineMap = new HashMap<>();

            for(int i = 0; i < magazine.length; i++){
               if (!magazineMap.containsKey(magazine[i])){
                   magazineMap.put(magazine[i],1);
                }else{
                   magazineMap.replace(magazine[i],magazineMap.get(magazine[i])+1);
               }//else
            }//for to map magazine

            String message ="Yes";
            for(int j = 0; j < ransom.length; j++){
                if(magazineMap.containsKey(ransom[j])&& (magazineMap.get(ransom[j])>0)){
                    magazineMap.replace(ransom[j],magazineMap.get(ransom[j])-1);
                }//if magazine contain word
                else{
                    message ="No";
                    break;
                }//else we return "No" because there is no more word in magazine that can be used for ransom
            }//for to check ransom against Magazine map

            System.out.print(message);
        }//else when m >=n

    }//main
}//class

