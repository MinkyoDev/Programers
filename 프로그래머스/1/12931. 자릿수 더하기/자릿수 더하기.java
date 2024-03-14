import java.util.*;

public class Solution {
    public int solution(int n) {
        String str = Integer.toString(n);
        int total = 0;
        
        for (char ch : str.toCharArray()) {
        	total += Character.getNumericValue(ch);
        }
        return total;
    }
}