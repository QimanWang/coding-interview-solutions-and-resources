/**
 * Created by qiman on 1/11/2017.
 */
public class CountingBinarySubstrings {
/*
 * Complete the function below.
 */

    static int counting(String s) {

        int numSubString = 0;
        String front=Character.toString(s.charAt(0));
        String back ="";
        if(Character.toString(s.charAt(1) ==Character.toString(s.charAt(0)){
            back = front; }
        else{back = Character.toString(s.charAt(1)}

        int numFront =0;
        int numBack =0;

        for(int i =3; i <s.length(); i++){
            //if

            //if char same a
            if(numback==0){
                if (Character.toString(s.charAt(i))==Character.toString(front.charAt(front.length()-1))){
                    front+= Character.toString(s.charAt(i)); numFront++;
                }else {
                    back+= Character.toString(s.charAt(i)); numBack++;}
            }//if
            if(front == back){numSubString++;}//

            // if(front!=back&& numFront == numBack){numSubString++;}

        }//fori
        return numSubString;
    }//counting
   /*10001 - 2
     00110 - 3
     10101 - 4
   */
    public static void main (String args[]){
        System.out.println(counting());
    }

}//class
