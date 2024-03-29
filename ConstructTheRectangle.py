"""
A web developer needs to know how to design a web page's size. So, given a specific rectangular web page's area, your job by now is to design a rectangular web page, 
whose length L and width W satisfy the following requirements:

    1. The area of the rectangular web page you designed must equal to the given target area.
    2. The width W should not be larger than the length L, which means L >= W.
    3. The difference between length L and width W should be as small as possible.

Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.
"""

class ConstructTheRectangle(object):
    def constructRectangle(self, area):
        width = (int)(area ** 0.5)
        while area % width != 0:
            width -= 1
        return [area / width, width]
        
        