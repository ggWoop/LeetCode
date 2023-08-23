class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for x in range(n)] for y in range(m)]
        for row in dp:
            print(row)
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    # 왼쪽 칸에서 오른쪽 칸으로 이동하는 방법 밖에 없음

                    dp[i][j] = dp[i][j-1]

                    pass
                elif j == 0:
                    # 위 칸에서 아래로 이동하는 방법 밖에 없음
                    dp[i][j] = dp[i-1][j]
                    pass
                else:
                    # 위에서 내려오거나 왼쪽에서 오른쪽으로 이동하거나
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                    pass
        return dp[-1][-1]