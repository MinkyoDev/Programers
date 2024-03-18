class Solution {
    public int solution(int a, int b) {
        int num1 = Integer.parseInt(String.valueOf(a) + String.valueOf(b));
		int num2 = a * b * 2;
		return Integer.max(num1, num2);
    }
}