import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Boj2606 {
    public static int total = 0;
    
    public static void BFS(int n, List<Integer>[] graph) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);

        boolean[] visited = new boolean[n+1];
        Arrays.fill(visited, false);

        while (!queue.isEmpty()) {
            int now = queue.poll();

            if (!visited[now]) {
                visited[now] = true;
                total++;

                for (int next : graph[now]) {
                    if (!visited[next]) {
                        queue.add(next);
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());
        int m = Integer.parseInt(bf.readLine());

        List<Integer>[] graph = new ArrayList[n+1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
            graph[b].add(a);
        }

        BFS(n, graph);

        System.out.println(total-1);
    }
}
