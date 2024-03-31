import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void Solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		long data = Long.parseLong(br.readLine());
		long result = (long) Math.sqrt(data);
		
		if((result*result) < data) result++;
		
		System.out.println(result);
	}

	public static void main(String[] args) throws Exception {
		new Main().Solution();
	}
}
