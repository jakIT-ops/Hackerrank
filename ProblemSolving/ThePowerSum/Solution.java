import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {

    /*
     * Complete the 'powerSum' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER X
     *  2. INTEGER N
     */

    static int [][] subTasks = new int[1001][33];

    static int maxMember;

    static int Rec(int X, int N, int start){
    	if(X == 0) return 1;
	if(X < 0) return 0;
	if(start > maxMember) return 0;

	int sum;
	if(subTasks[X][start] != 0) return subTasks[X][start];
	else {
		sum = Rec(X, N, start+1) + Rec(X - (int)Math.pow(start, N), N, start+1);

		subTasks[X][start] = sum;
		
		return sum;
	}
    }
    public static int powerSum(int X, int N) {
    	// Write your code here
    	maxMember = (int)Math.pow(X, 1.0/N);

	return Rec(X, N, 0);
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int X = Integer.parseInt(bufferedReader.readLine().trim());

        int N = Integer.parseInt(bufferedReader.readLine().trim());

        int result = Result.powerSum(X, N);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
