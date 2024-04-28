import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void Solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int[] block = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		int N = Integer.parseInt(br.readLine());

		int[] points = new int[N];
		for (int i = 0; i < N; i++) {
			int[] pointCorr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
			points[i] = getPosition(block, pointCorr);
		}

		int[] originCorr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		int origin = getPosition(block, originCorr);

		int total = 0;
		for (int i = 0; i < N; i++) {
			total += distance(block, origin, points[i]);
		}

		System.out.println(total);
	}

	public static int distance(int[] block, int origin, int point) {
		int end = (block[0] + block[1]) * 2;
		int distance1 = Math.abs(origin - point);
		int distance2 = end - Math.max(origin, point) + Math.min(origin, point);
		return Math.min(distance1, distance2);

	}

	public static int getPosition(int[] block, int[] point) {
		int value = 0;
		switch (point[0]) {
		case 1 : {
			value = point[1];
			break;
		}
		case 4 : {
			value = point[1] + block[0];
			break;
		}
		case 2 : {
			value = (block[0] - point[1]) + block[0] + block[1];
			break;
		}
		case 3 : {
			value = (block[1] - point[1]) + block[0] + block[0] + block[1];
			break;
		}
		}
		return value;
	}

	public static void main(String[] args) throws Exception {
		new Main().Solution();
	}
}