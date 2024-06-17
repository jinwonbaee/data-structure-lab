# 프로젝트 문제 3번
input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []
from collections import deque
def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0
    # 입력 힌트

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]
    
    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))

    #여기에서부터 코드를 작성하세요.
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(x, y, size):
        visited = [[False] * N for _ in range(N)]
        queue = deque([(x, y, 0)])
        visited[x][y] = True
        edible_hives = []

        while queue:
            cx, cy, dist = queue.popleft()
            for d in range(4):
                nx, ny = cx + dx[d], cy + dy[d]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if forest[nx][ny] <= size:
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))
                        if 0 < forest[nx][ny] < size:
                            edible_hives.append((dist + 1, nx, ny))
        
        if edible_hives:
            edible_hives.sort()
            return edible_hives[0]
        else:
            return None

    # 시뮬레이션
    while True:
        result = bfs(bear_x, bear_y, bear_size)
        if result is None:
            break
        dist, nx, ny = result
        time += dist
        bear_x, bear_y = nx, ny
        forest[nx][ny] = 0
        honeycomb_count += 1
        if honeycomb_count == bear_size:
            bear_size += 1
            honeycomb_count = 0

    return time

result = problem3(input)

assert result == 14
print("정답입니다.")