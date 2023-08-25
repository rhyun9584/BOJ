import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Boj1182 {
    public static int n;
    public static int s;
    public static int[] number;
    public static int result = 0;

    public static void search(int idx, int total, boolean canCheck) {
        if (total == s && canCheck) {
            result++;
        }

        if (idx == n) {
            return;
        }

        search(idx+1, total+number[idx], true);
        search(idx+1, total, false);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());

        number = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            number[i] = Integer.parseInt(st.nextToken());
        }

        search(0, 0, false);

        System.out.println(result);
    }
}
