"""
    There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

    The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot 
    returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

    Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that 
    the magnitude of the robot's movement is the same for each move.
"""

class RobotReturnToOrigin(object):
    def judgeCircle(self, moves):
        direction = {}
        direction['U'] = 0
        direction['D'] = 0
        direction['L'] = 0
        direction['R'] = 0
        for i in range(0, len(moves)):
            direction[moves[i]] += 1
        return direction['U'] == direction['D'] and direction['L'] == direction['R']