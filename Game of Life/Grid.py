import pygame
from numpy import arange
from GameValues import WHITE, WIDTH, HEIGHT, Grid, GridPos, SqS
from AbstractCl import Square


class GridSquare(Square):
    
    def __init__(self, pos, group, alpha):
        super().__init__(pos, group)
        pygame.draw.aalines(self.image, WHITE, True,  self.SquareCorners())
        self.image.set_alpha(alpha)
        

    def SquareCorners(self):
        corners = []
        corners.append([0, self.a])
        corners.append([0, 0])
        corners.append([self.a, 0])
        corners.append([self.a, self.a])
        return corners
    
    
def GenerateGrid():
    line = []
    for j in arange(1, WIDTH-SqS , SqS):
        for i in arange(1, HEIGHT-SqS, SqS):
            GridSquare([j + SqS// 2, i + SqS // 2], Grid, 44)
            line.append([j + SqS// 2, i + SqS // 2])
        GridPos.append(line)
        line = []



