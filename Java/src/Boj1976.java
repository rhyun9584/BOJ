import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Boj1976 {
    public static int[] parent;

    public static int findParent(int x) {
        if (parent[x] != x) {
            parent[x] = findParent(parent[x]); 
        }

        return parent[x];
    }

    public static void union(int x, int y) {
        int parentX = findParent(x);
        int parentY = findParent(y);

        if (parentX < parentY) {
            parent[parentY] = parentX;
        } else {
            parent[parentX] = parentY;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        StringTokenizer st;

        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());    
            for (int j = 0; j < N; j++) {
                int edge = Integer.parseInt(st.nextToken());

                if (edge == 1) {
                    union(i, j);
                }
            }
        }

        st = new StringTokenizer(br.readLine());

        int[] plan = new int[M];
        for (int i = 0; i < M; i++) {
            plan[i] = Integer.parseInt(st.nextToken())-1;
        }

        String result = "YES";
        for (int i = 1; i < M; i++) {
            if (findParent(plan[0]) != findParent(plan[i])) {
                result = "NO";
                break;
            }
        }

        System.out.println(result);
    }
}
