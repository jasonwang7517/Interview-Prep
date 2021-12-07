"""
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells 
(i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average 
(i.e., the average of the four cells in the red smoother).
"""

class ImageSmoother(object):
    def imageSmoother(self, img):
        M = img
        row, col = len(M), len(M[0])
        res = [[0]*col for i in range(row)]
        dirs = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        for i in range(row):
            for j in range(col):
                temp = [M[i+m][j+n] for m,n in dirs if 0<=i+m<row and 0<=j+n<col]
                res[i][j] = sum(temp)//len(temp)
        return res
        
                
        