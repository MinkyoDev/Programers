import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

	public static void Solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int data = Integer.parseInt(br.readLine());
		int result = 0;

		for (int i = 0; i < data; i++) {
			int total = i;
			for (char ch : String.valueOf(i).toCharArray()) {
				total += Character.getNumericValue(ch);
			}
			if (total == data) {
				result = i;
				break;
			}
		}

		bw.write(String.valueOf(result));
		bw.newLine();
		bw.flush();
	}

	public static void main(String[] args) throws Exception {
		new Main().Solution();
	}
}