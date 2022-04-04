package GraphBFSDFS.boj_13460_ballEscape_1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static class BallPoint {
        int x, y;

        public BallPoint(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    static class BallQueue {
        BallPoint red;
        BallPoint blue;
        int moved = 0;

        public BallQueue(BallPoint red, BallPoint blue, int moved) {
            this.red = red;
            this.blue = blue;
            this.moved = moved;
        }
    }

    static int answer = -1;
    static int sizeY, sizeX;
    static Character[][] map;
    static BallPoint red, blue;
    static ArrayDeque<BallQueue> queue = new ArrayDeque<BallQueue>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        sizeY = Integer.parseInt(st.nextToken());
        sizeX = Integer.parseInt(st.nextToken());
        map = new Character[sizeY][sizeX];

        for (int indexY = 0; indexY < sizeY; ++indexY) {
            st = new StringTokenizer(br.readLine());
            String data = st.nextToken();

            for (int indexX = 0; indexX < data.length(); ++indexX) {
                map[indexY][indexX] = data.charAt(indexX);
                if (map[indexY][indexX].equals('B')) {
                    blue = new BallPoint(indexY, indexX);
                    map[indexY][indexX] = '.';
                } else if (map[indexY][indexX].equals('R')) {
                    red = new BallPoint(indexY, indexX);
                    map[indexY][indexX] = '.';
                }
            }

        }

//        BFS
        queue.push(new BallQueue(red, blue, 0));

//        System.out.println(Arrays.deepToString(map));
//        System.out.println(red.y + " " + red.x);

        while (queue.size() > 0) {
            BallQueue curStatus = queue.pollFirst();
            red = curStatus.red;
            blue = curStatus.blue;
//            System.out.println(red.y + " " + red.x + " " + blue.y + " " + blue.x + " " + curStatus.moved);
            if (curStatus.moved > 10) {
                break;
            } else if (blue.x == -1 && blue.y == -1) {
                continue;
            } else if (red.y == -1 && red.x == -1) {
                answer = (answer == -1) ? curStatus.moved : answer;
                break;
            } else {
                for (int dir = 0; dir < 4; ++dir) {
                    BallQueue nextAdd = nextQueue(dir, curStatus.moved);
                    if (red.x != nextAdd.red.x || red.y != nextAdd.red.y || blue.x != nextAdd.blue.x|| blue.y != nextAdd.blue.y) {
                        queue.add(nextAdd);
                    }
                }
            }

        }

        System.out.println(answer);

    }

    static public BallQueue nextQueue(int dir, int curMoves) {
        BallPoint nextRed = new BallPoint(red.y, red.x);
        BallPoint nextBlue = new BallPoint(blue.y, blue.x);
//        dir0 left, dir1 right, dir2 up, dir3 down
        if (dir == 0) {
            if (nextRed.x < nextBlue.x) {
                nextRed = moveBalls(nextRed, nextBlue, 0, -1);
                nextBlue = moveBalls(nextBlue, nextRed, 0, -1);
            } else {
                nextBlue = moveBalls(nextBlue, nextRed, 0, -1);
                nextRed = moveBalls(nextRed, nextBlue, 0, -1);
            }
        } else if (dir == 1) {
            if (nextRed.x > nextBlue.x) {
                nextRed = moveBalls(nextRed, nextBlue, 0, 1);
                nextBlue = moveBalls(nextBlue, nextRed, 0, 1);
            } else {
                nextBlue = moveBalls(nextBlue, nextRed, 0, 1);
                nextRed = moveBalls(nextRed, nextBlue, 0, 1);
            }
        } else if (dir == 2) {
            if (nextRed.y < nextBlue.y) {
                nextRed = moveBalls(nextRed, nextBlue, -1, 0);
                nextBlue = moveBalls(nextBlue, nextRed, -1, 0);
            } else {
                nextBlue = moveBalls(nextBlue, nextRed, -1, 0);
                nextRed = moveBalls(nextRed, nextBlue, -1, 0);
            }
        } else {
            if (nextRed.y > nextBlue.y) {
                nextRed = moveBalls(nextRed, nextBlue, 1, 0);
                nextBlue = moveBalls(nextBlue, nextRed, 1, 0);
            } else {
                nextBlue = moveBalls(nextBlue, nextRed, 1, 0);
                nextRed = moveBalls(nextRed, nextBlue, 1, 0);
            }
        }
        return new BallQueue(nextRed, nextBlue, curMoves + 1);
    }

    static public BallPoint moveBalls(BallPoint moveBall, BallPoint fixedBall, int dy, int dx) {
        while (true) {
            if (moveBall.y + dy == fixedBall.y && moveBall.x + dx == fixedBall.x) {
                break;
            } else if (map[moveBall.y + dy][moveBall.x + dx].equals('.')) {
                moveBall.y += dy;
                moveBall.x += dx;
            } else if (map[moveBall.y + dy][moveBall.x + dx].equals('O')) {
                moveBall.y = -1;
                moveBall.x = -1;
                break;
            } else {
                break;
            }
        }
        return moveBall;
    }
}
