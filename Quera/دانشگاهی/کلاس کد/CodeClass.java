import java.util.*;
class CodeClass{
    public static void main(String args[]){
        String number = "";
        Scanner scan = new Scanner(System.in);  
        int k = scan.nextInt(); // input from user
        for(int i=1; i<=5000; i++)
            number = number + String.valueOf(i);
        for(int i=1; i<=number.length(); i++){
            if(k == i){
                System.out.println(number.charAt(i-1));
                break;
            }
        }
        scan.close();
    }
}