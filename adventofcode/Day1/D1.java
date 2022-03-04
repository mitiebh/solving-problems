package Day1;
import java.io.*;
public class D1{

    static void part2() throws Exception{

    }
    static void part1() throws Exception{
        File file = new File
        ("...your path\\inputs.txt");
        BufferedReader bfr = new BufferedReader(new FileReader(file));

        int counter = 0;
        String nextInput;
        String input1 = bfr.readLine();
        while((nextInput = bfr.readLine()) != null){
            if(Integer.parseInt(nextInput) > Integer.parseInt(input1)){
                counter++; // incressed
                input1 = nextInput;
            }
            else
                input1 = nextInput;
        }
        System.out.println(counter);
        bfr.close();
    }
    public static void main(String args[]) throws Exception {
        //part1();
        part2();
    }
}