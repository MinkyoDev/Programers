import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public static int solution(int a, int b) {
		int num1 = Integer.parseInt(Integer.toString(a) + Integer.toString(b));
		int num2 = Integer.parseInt(Integer.toString(b) + Integer.toString(a));
		return Integer.max(num1, num2);
	}
}