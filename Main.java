import java.math.BigDecimal;
import java.math.BigInteger;

public class Main {


    public static void main(String[] args){
        // "#4dad4b", # greenish
        // "#4dad4b", # greenish
        // "#15d8ed", # light blue
        // "#AB65DD", # purple
        // "#FA4D7F", # pink
        // "#AB65DD", # purple
        // "#15d8ed", # light blue
        // "#4dad4b",  # greenish
        // "#4dad4b"  # greenish
        int[][] rgbList = {
            {77, 173, 75}, 
            {77, 173, 75}, 
            {21, 216, 237},
            {171, 101, 221},
            {250, 77, 127}, 
            {171, 101, 221},
            {21, 216, 237},
            {77, 173, 75}, 
            {77, 173, 75}
        };
        int[][] gradient = bezierGradient(rgbList, 18);
        for(int i = 0; i < gradient.length; i++){
            System.out.print("[");
            for(int j = 0; j < gradient[i].length; j++){
                System.out.print(gradient[i][j] + " ");
            }
            System.out.println("],");
        }
    }

    public static int[][] bezierGradient(int[][] rgbList, int numOut){
        int[][] gradient = new int[numOut][3];

        for(int t = 0; t < numOut; t++){
            gradient[t] = bezierInterp(rgbList, (double) t / (numOut - 1));
        }

        return gradient;
    }

    public static int[] bezierInterp(int[][] rgbList, double t){
        int n = rgbList.length; 
        int[][] summands = new int[n][3];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < 3; j++){
                summands[i][j] = (int) (bernstein(t, n, i) * rgbList[i][j]);
            }
        }

        int[] output = {0, 0, 0};
        for(int i = 0; i < summands.length; i++){
            for(int j = 0; j < 3; j++){
                output[j] += summands[i][j];
            }
        }

        return output;
    }

    public static double bernstein(double t, int n, int i){
        BigDecimal binom = calculateFactorial(n).divide(calculateFactorial(i).multiply(calculateFactorial(n - i)));
        return binom.multiply(new BigDecimal(1 - t).pow(n - i)).multiply(new BigDecimal(t).pow(i)).doubleValue();
    }

    // https://www.hackerearth.com/practice/notes/efficient-factorials-calculation/
    private static BigDecimal calculateFactorial(int uptoValue) {
        BigInteger answer = BigInteger.ONE;
        boolean oddUptoValue = ((uptoValue & 1) == 1);
        int tempUptoValue = uptoValue;
        if(oddUptoValue){
            tempUptoValue = uptoValue - 1;
        }

        int nextSum = tempUptoValue;
        int nextMulti = tempUptoValue;
        while (nextSum >= 2){
            answer = answer.multiply(BigInteger.valueOf(nextMulti));
            nextSum -= 2;
            nextMulti += nextSum;
        }

        if(oddUptoValue){
            answer = answer.multiply(BigInteger.valueOf(uptoValue));
        }

        return new BigDecimal(answer);
    }
}