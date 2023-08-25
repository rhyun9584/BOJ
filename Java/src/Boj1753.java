import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Boj1753 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        int start = Integer.parseInt(br.readLine());
        
        List<int[]>[] graph = new ArrayList[V+1];
        for (int i = 0; i <= V; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());

            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            int[] list = {v, w};
            graph[u].add(list);
        }

        int[] dist = new int[V+1];
        Arrays.fill(dist, Integer.MAX_VALUE);

        PriorityQueue<int[]> queue = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0]) {
                    return o1[1] - o2[1];
                }

                return o1[0] - o2[0];
            }
        });
        int[] startList = {0, start};
        queue.add(startList);

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            int cost = now[0];
            int v = now[1];

            if (cost >= dist[v]) {
                continue;
            }

            dist[v] = cost;

            for (int[] next: graph[v]) {
                if (cost + next[1] < dist[next[0]]) {
                    int[] addNext = {cost+next[1], next[0]};
                    queue.add(addNext);
                }
            }
        }

        for (int i = 1; i <= V; i++) {
            System.out.println(dist[i] == Integer.MAX_VALUE ? "INF" : dist[i]);
        }
    }   
}
