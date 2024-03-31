import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void Solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int k = Integer.parseInt(br.readLine());
		int[] result = { 0, 1 };

		for (int i = 1; i < k; i++) {
			int tmp = result[0] + result[1];
			result[0] = result[1];
			result[1] = tmp;
		}

		System.out.println(result[0] + " " + result[1]);
	}

	public static void main(String[] args) throws Exception {
		new Main().Solution();
	}
}
