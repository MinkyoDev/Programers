class Solution {
    public int solution(int[] num_list) {
		String odd = "";
		String even = "";
		for (int num : num_list) {
			odd += num % 2 == 1 ? String.valueOf(num) : "";
			even += num % 2 == 0 ? String.valueOf(num) : "";
		}
		return Integer.parseInt(odd) + Integer.parseInt(even);
	}
}