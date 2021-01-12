class Solution(object):
    def judgeCircle(self, moves):
        direction = {}
        direction['U'] = 0
        direction['D'] = 0
        direction['L'] = 0
        direction['R'] = 0
        for i in range(0, len(moves)):
            direction[moves[i]] += 1
        return direction['U'] == direction['D'] and direction['L'] == direction['R']