class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
		int idx = 0;

		for (int[] querie : queries) {
			int temp = 1000000;
			for (int i = querie[0]; i <= querie[1]; i++) {
				if (querie[2] < arr[i] && arr[i] < temp) {
					temp = arr[i];
				}
			}
			answer[idx] = temp == 1000000 ? -1 : temp;
			idx++;
		}

		return answer;
    }
}