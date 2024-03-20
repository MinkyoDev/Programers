class Solution {
    public String solution(String code) {
        char[] arr = code.toCharArray();
		boolean mode = false;
		String answer = "";

		for (int i = 0; i < arr.length; i++) {
			if (!mode) {
				if (arr[i] == '1') {
					mode = true;
				} else {
					answer += i % 2 == 0 ? arr[i] : "";
				}
			} else {
				if (arr[i] == '1') {
					mode = false;
				} else {
					answer += i % 2 == 1 ? arr[i] : "";
				}
			}
		}
		return answer == "" ? "EMPTY" : answer;
    }
}