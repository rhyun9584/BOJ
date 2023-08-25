import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


class Point2573 {
    int r;
    int c;

    Point2573(int r, int c) { 
        this.r = r;
        this.c = c;
    }
}

public class Boj2573 {
    public static int n;
    public static int m;
    public static int[][] board;
    public static boolean[][] visited;
    public static Queue<Point2573> iceberg;
    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static void BFS(int sr, int sc) {
        Queue<Point2573> queue = new LinkedList<>();
        queue.add(new Point2573(sr, sc));

        while (!queue.isEmpty()) {
            Point2573 now = queue.poll();

            if (visited[now.r][now.c]) {
                continue;
            }

            visited[now.r][now.c] = true;

            for (int i = 0; i < 4; i++){
                int nextR = now.r + dr[i];
                int nextC = now.c + dc[i];

                if (nextR > 0 && nextR < n-1 && nextC > 0 && nextC < m-1 && board[nextR][nextC] > 0 && !visited[nextR][nextC]) {
                    queue.add(new Point2573(nextR, nextC));
                }
            }
        }
    }

    public static boolean isDivided() {
      // 방문 확인 배열 초기화    
        for (int i = 0; i < n; i++) {
            Arrays.fill(visited[i], false);
        }

        // BFS로 빙산 덩어리 수 확인
        int count = 0;
        for (int i = 1; i < n-1; i++) {
            for (int j = 1; j < m-1; j++) {
                if (board[i][j] > 0 && !visited[i][j]) {
                    if (count > 0) {
                        return true;
                    }

                    count++;
                    BFS(i, j);
                }
            }
        }

        return false;
    }

    public static void sink() {
        Queue<int[]> sink = new LinkedList<>();

        while (!iceberg.isEmpty()) {
            Point2573 now = iceberg.poll();

            int zeroCount = 0;
            for (int i = 0; i < 4; i++){
                int roundR = now.r + dr[i];
                int roundC = now.c + dc[i];

                if (roundR >= 0 && roundR < n && roundC >= 0 && roundC < m && board[roundR][roundC] == 0){
                    zeroCount++;
                }
            }

            int[] list = {now.r, now.c, zeroCount};
            sink.add(list);
        }

        while (!sink.isEmpty()) {
            int[] list = sink.poll();

            if (list[2] == 0) {
                iceberg.add(new Point2573(list[0], list[1]));
            } else {
                board[list[0]][list[1]] = Math.max(0, board[list[0]][list[1]] - list[2]);

                if (board[list[0]][list[1]] > 0) {
                    iceberg.add(new Point2573(list[0], list[1]));
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        iceberg = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++){
                board[i][j] = Integer.parseInt(st.nextToken());

                if (board[i][j] > 0){
                    iceberg.add(new Point2573(i, j));
                }
            }
        }

        visited = new boolean[n][m];

        int year = 0;
        while (!isDivided()) {
            year++;

            sink();
            
            if (iceberg.isEmpty()){
                year = 0;
                break;
            }
        }

        System.out.println(year);
    }
}
