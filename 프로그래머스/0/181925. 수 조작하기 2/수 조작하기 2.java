class Solution {
    public static String solution(int[] numLog) {
		String result = "";
		for (int i = 1; i < numLog.length; i++) {
			int temp = numLog[i] - numLog[i - 1];
			switch (temp) {
			case 1-> {result += 'w';}
			case -1-> {result += 's';}
			case 10-> {result += 'd';}
			case -10-> {result += 'a';}
				
			}
		}
		return result;
	}
}