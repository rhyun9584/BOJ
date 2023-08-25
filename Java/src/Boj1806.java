import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Boj1806 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int[] number = new int[n];
        for (int i = 0; i < n; i++) {
            number[i] = Integer.parseInt(st.nextToken());
        }

        int[] S = new int[n+1];
        S[0] = 0;
        for (int i = 1; i <= n; i++) {
            S[i] = S[i-1] + number[i-1];
        }

        int start = 0;
        int end = 1;

        int answer = n+1;
        while (end <= n) {
            if (s <= S[end] - S[start]) {
                answer = Math.min(answer, end - start);
                start++;
            } else {
                end++;
            }
        }

        if (answer == n+1) {
            answer = 0;
        }
        System.out.println(answer);
    }
    
}
