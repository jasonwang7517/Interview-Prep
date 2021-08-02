"""
    An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

    You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

    To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
    plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

    Return the modified image after performing the flood fill.
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R = len(image)
        C = len(image[0])
        color = image[sr][sc]
        if color == newColor: 
            return image
        def dfs(rows, cols):
            if image[rows][cols] == color:
                image[rows][cols] = newColor
                if rows >= 1: 
                    dfs(rows - 1, cols)
                if rows + 1 < R: 
                    dfs(rows + 1, cols)
                if cols >= 1: 
                    dfs(rows, cols - 1)
                if cols + 1 < C: 
                    dfs(rows, cols + 1)
        dfs(sr, sc)
        return image