import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void Solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int[] arr = new int[9];
		for (int i = 0; i < 9; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		int sum = Arrays.stream(arr).sum();
		int no1 = 0, no2 = 0;

		Loop1: for (int i = 0; i < 8; i++) {
			for (int j = i + 1; j < 9; j++) {
				if (arr[i] + arr[j] == sum - 100) {
					no1 = arr[i];
					no2 = arr[j];
					break Loop1;
				}
			}
		}
		int no11 = no1, no22 = no2;
		Arrays.stream(arr).filter(i -> i != no11).filter(i -> i != no22).sorted().forEach(i->System.out.println(i));
	}

	public static void main(String[] args) throws Exception {
		new Main().Solution();
	}
}