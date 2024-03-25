import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public static int[] solution(int[] num_list) {
		ArrayList<Integer> arr = new ArrayList<Integer>();

		for (int i = 0; i < num_list.length + 1; i++) {
			if (i > num_list.length - 1) {
				int result = num_list[i - 1] - num_list[i - 2];
				arr.add(result > 0 ? result : num_list[i - 1] * 2);
			} else {
				arr.add(num_list[i]);
			}
		}

		return arr.stream().mapToInt(Integer::intValue).toArray();
	}
}