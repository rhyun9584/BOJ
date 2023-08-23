import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


class Point {
    int x;
    int y;
    int count;

    Point(int x, int y, int count) {
        this.x = x;
        this.y = y;
        this.count = count;
    }
}

public class Boj2178 {

    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static int BFS(int n, int m, char[][] board) {
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(0, 0, 1));

        boolean[][] visited = new boolean[n][m];
        for (int i = 0; i < n; i++){
            Arrays.fill(visited[i], false);
        }
        
        while (!queue.isEmpty()) {
            Point now = queue.poll();
            
            int nowX = now.x;
            int nowY = now.y;

            if (nowX == n-1 && nowY == m-1) {
                return now.count;
            }
            
            if (!visited[nowX][nowY]) {
                visited[nowX][nowY] = true;

                for (int i = 0; i < 4; i++){
                    int nextX = nowX + dx[i];
                    int nextY = nowY + dy[i];

                    if (nextX >= 0 && nextX < n && nextY >= 0 && nextY < m && board[nextX][nextY] == '1' && !visited[nextX][nextY]) {
                        queue.add(new Point(nextX, nextY, now.count+1));
                    }
                }
            }
        }

        return 0;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        char[][] board = new char[n][m];
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().toCharArray();
        }

        System.out.println(BFS(n, m, board));
    }
}
