import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	static int[] arr;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] input = br.readLine().split(" ");
		int N = Integer.parseInt(input[0]);
		int M = Integer.parseInt(input[1]);

		arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

		int sum = Arrays.stream(arr).sum();
		int max = Arrays.stream(arr).max().getAsInt();

		System.out.println(binarySearch2(M, max, sum));
	}

	static int binarySearch2(int key, int low, int high) {
		while (low <= high) {
            int mid = (low + high) / 2;

            int count = getCount(mid);

            if(count > key){
            	low = mid + 1;
            }else{
            	high = mid - 1;
            }
        }

		return low;
	}

	private static int getCount(int mid) {
		int sum = 0;
		int count = 0;
		for (int i = 0; i < arr.length; i++) {
			if (sum + arr[i] > mid) {
				sum = 0;
				count++;
			}
			sum += arr[i];
		}

		if (sum != 0)
			count++;
		return count;
	}
}