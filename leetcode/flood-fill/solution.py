class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        curr_color = image[sr][sc]
        height = len(image)
        width = len(image[0])

        def dfs(sr,sc):
            if 0 <= sr < height and 0 <= sc < width and image[sr][sc] ==  curr_color and image[sr][sc] != color :
                image[sr][sc] = color

                dfs(sr+1,sc)
                dfs(sr-1,sc)
                dfs(sr,sc+1)
                dfs(sr,sc-1)
        dfs(sr,sc)
        return image