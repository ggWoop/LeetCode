class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque


# 방문한 좌표 체크: 꺼낸 좌표가 이미 방문한 좌표인지 확인하고, 방문하지 않았다면 처리해야 합니다. 
# visited 세트를 사용하여 이를 확인할 수 있습니다.

# 유효한 좌표 확인: 새로운 좌표가 이미지의 범위 내에 있는지 확인하고, 
# 해당 좌표의 색상이 시작 색상과 같은지 확인해야 합니다.

# 색상 변경: 유효한 좌표인 경우, 해당 좌표의 색상을 새 색상으로 변경해야 합니다.

# 새로운 좌표 추가: 새로운 좌표가 유효하면 큐에 추가하고, 방문 목록에도 추가해야 합니다.


        src_color = image[sr][sc]
        q = deque([(sr, sc)])
        visited = set()
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            cur_y, cur_x = q.popleft()
            # 꺼내온 좌표가 이미 방문한 좌표인지 아닌지 체크
            if (cur_y, cur_x) in visited:
                continue
            visited.add((cur_y, cur_x))
            # 만약 유효한 좌표라면 image에서 색상을 바꿔줄 것
            image[cur_y][cur_x] = color
            for move in moves:
                # 이동할 좌표 계산, 이동 가능한지 체크하고, 큐에 넣어줌
                new_y = cur_y + move[0]
                new_x = cur_x + move[1]
                if new_y < 0 or new_y > len(image) -1:
                    continue
                if new_x < 0 or new_x > len(image[0]) -1:
                    continue
                if image[new_y][new_x] == src_color:
                    q.append((new_y, new_x))
        return image



