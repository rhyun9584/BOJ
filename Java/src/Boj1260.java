import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


public class Boj1260 {
    public static void DFS(int n, int v, List<Integer>[] graph) {
        Stack<Integer> stack = new Stack<>();
        stack.push(v);

        boolean[] visited = new boolean[n+1];
        Arrays.fill(visited, false);

        while (!stack.isEmpty()) {
            int now = stack.pop();

            if (!visited[now]) {
                visited[now] = true;
                System.out.print(now + " ");

                for (int next : graph[now]) {
                    if (!visited[next]){
                        stack.push(next);
                    }
                }
            }
        }
        System.out.println();
    }

    public static void BFS(int n, int v, List<Integer>[] graph) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(v);

        boolean[] visited = new boolean[n+1];
        Arrays.fill(visited, false);

        while (!queue.isEmpty()) {
            int now = queue.poll();

            if (!visited[now]) {
                visited[now] = true;
                System.out.print(now + " ");

                for (int next : graph[now]) {
                    if (!visited[next]) {
                        queue.add(next);
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        List<Integer>[] graph = new ArrayList[n+1];
        for (int i = 1; i < n+1; i++){
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m ; i++){
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
            graph[b].add(a);
        }

        for (int i = 1; i < n+1; i++) {
            graph[i].sort(Comparator.reverseOrder());
        }
        DFS(n, v, graph);

        for (int i = 1; i < n+1; i++) {
            graph[i].sort(Comparator.naturalOrder());
        }
        BFS(n, v ,graph);
    }
}