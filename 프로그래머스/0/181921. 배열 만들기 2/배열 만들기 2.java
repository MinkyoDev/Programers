import java.util.ArrayList;

class Solution {
    public static int[] solution(int l, int r) {
		ArrayList<Integer> arr = new ArrayList<>();

		for (int i = l; i <= r; i++) {
			boolean bool = true;
			for (char ch : String.valueOf(i).toCharArray()) {
				if (ch != '0' && ch != '5') {
					bool = false;
					break;
				}
			}
			if (bool) {
				arr.add(i);
			}
		}
		if (arr.size()==0) {
			arr.add(-1);
		}
		return arr.stream().mapToInt(Integer::intValue).toArray();
	}
}