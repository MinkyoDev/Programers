import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;


public class Main {

	public static void Solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String[] data = br.readLine().split(" ");
		String[] arr = Arrays.stream(data).mapToInt(s->Integer.parseInt(s)).sorted().mapToObj(String::valueOf).toArray(String[]::new);
		
		bw.write(String.valueOf(String.join(" ", arr)));
		bw.newLine();
		bw.flush();
	}

	public static void main(String[] args) throws Exception {
		new Main().Solution();
	}
}
