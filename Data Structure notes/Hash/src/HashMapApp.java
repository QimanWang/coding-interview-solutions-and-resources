import java.util.HashMap;
import java.util.Map;

/**
 * Created by qiman on 1/10/17.
 */
public class HashMapApp {
    public static void main(String args[]){

        HashMap<String,Integer> map = new HashMap();

        map.put("alice", 111);
        map.put("bob", 222);

        for(String key: map.keySet()){
            System.out.println(key);
        }
        for(Integer value: map.values()){
            System.out.println(value);
        }
        for( Map.Entry<String, Integer> entry : map.entrySet()){
            String key = entry.getKey();
            Integer value = entry.getValue();
            System.out.println(key+" "+value);
        }

    }//main
}//hashMapApp
