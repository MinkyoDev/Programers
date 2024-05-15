import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	static int max = 0;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

		permutation(arr, 0, N, N);

		System.out.println(max);
	}

	static void permutation(int[] arr, int depth, int n, int r) {
		if (depth == r) {
			print(arr);
			return;
		}

		for (int i = depth; i < n; i++) {
			swap(arr, depth, i);
			permutation(arr, depth + 1, n, r);
			swap(arr, depth, i);
		}
	}

	static void swap(int[] arr, int depth, int i) {
		int temp = arr[depth];
		arr[depth] = arr[i];
		arr[i] = temp;
	}

	static void print(int[] arr) {
		int total = 0;
		for (int i = 0; i < arr.length - 1; i++) {
			total += Math.abs(arr[i] - arr[i + 1]);
		}
		if (total > max) {
			max = total;
		}
	}
}