import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Boj2667 {
    public static int n;
    public static char[][] board;
    public static boolean[][] visited;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static int BFS(int sx, int sy) {
        Queue<int[]> queue = new LinkedList<>();

        int[] start = {sx, sy};
        queue.add(start);

        int total = 0;
        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            if(!visited[now[0]][now[1]]) {
                visited[now[0]][now[1]] = true;
                total++;

                for (int i = 0; i < 4; i++){
                    int[] next = {now[0]+dx[i], now[1]+dy[i]};

                    if (next[0] >= 0 && next[0] < n && next[1] >= 0 && next[1] < n && board[next[0]][next[1]] == '1' && !visited[next[0]][next[1]]) {
                        queue.add(next);
                    }
                }
            }
        }

        return total;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        
        board = new char[n][n];
        for (int i = 0; i < n; i++){
            board[i] = br.readLine().toCharArray();
        }

        visited = new boolean[n][n];
        for (int i = 0; i < n; i++){
            Arrays.fill(visited[i], false);
        }

        int total = 0;
        List<Integer> count = new ArrayList<>();
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '1' && !visited[i][j]) {
                    total++;
                    count.add(BFS(i, j));
                }
            }
        }

        count.sort(Comparator.naturalOrder());

        System.out.println(total);
        for (int c : count) {
            System.out.println(c);
        }
    }
}
