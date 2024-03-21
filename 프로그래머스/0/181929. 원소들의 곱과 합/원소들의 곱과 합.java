class Solution {
    public int solution(int[] num_list) {
		int sum = 0;
		int pac = 1;
		for (int num :num_list) {
			sum += num;
			pac *= num;
		}
		return sum*sum>pac?1:0;
	}
}