import java.util.*;
public class ArrayListApp {
    public static void main(String args[]){

    List<String> list = new ArrayList<>();

    list.add("Alice");
    list.add("Bob");
    list.add("Christian");

    for(String s: list){
        System.out.println(s);
    }//for
        list.add(1,"kenny");
    for(String s: list){
        System.out.println(s);
    }//for

    }//main
}//ArrayListApp
