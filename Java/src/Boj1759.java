import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Boj1759 {
    public static int l;
    public static int c;
    public static String[] list;

    public static boolean isVowel(String ch) {
        if (ch.equals("a") || ch.equals("e") || ch.equals("i") || ch.equals("o") || ch.equals("u")) {
            return true;
        } else {
            return false;
        }
    }

    public static void solution(int idx, StringBuilder str, int con, int vowel) {
        if(str.length() == l) {
            if (con >= 2 && vowel >= 1) {
                System.out.println(str);
            }
            return;
        }

        if (idx == c) {
            return;
        }

        str.append(list[idx]);
        if (isVowel(list[idx])) {
            solution(idx+1, str, con, vowel+1);
        } else {
            solution(idx+1, str, con+1, vowel);
        }

        str.deleteCharAt(str.length()-1);
        solution(idx+1, str, con, vowel);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
        StringTokenizer st = new StringTokenizer(br.readLine());
        l = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        
        list = br.readLine().split(" ");
        Arrays.sort(list);
        
        solution(0, new StringBuilder(), 0, 0);
    }
}
