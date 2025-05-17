import pygame
import sys
import GameValues
import datetime
from Grid import GenerateGrid
from Cell import RedCell
from Environment import GenerateEnvironment, PosTracEnvironment

pygame.init()

sc = pygame.display.set_mode((GameValues.WIDTH, GameValues.HEIGHT))
clock = pygame.time.Clock()
print(GameValues.WIDTH // GameValues.SqS, GameValues.HEIGHT // GameValues.SqS)
GenerateGrid()
GenerateEnvironment()

testCell = RedCell(GameValues.GridPos[10][4], GameValues.RedCells)
testCell.CheckСonditions()
pygame.display.update()

while True:        
    clock.tick(GameValues.FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_RIGHT:
                testCell.rect.x += GameValues.SqS
            if event.key == pygame.K_LEFT:
                testCell.rect.x -= GameValues.SqS
            if event.key == pygame.K_g:
                GameValues.activeGrid = 1 - GameValues.activeGrid
            if event.key == pygame.K_c:
                GameValues.activeClouds = 1 - GameValues.activeClouds
            if event.key == pygame.K_r:
                GameValues.radiationMap = 1 - GameValues.radiationMap
            if event.key == pygame.K_SPACE:
                GameValues.pause = 1 - GameValues.pause
    
    if not GameValues.pause:
        
        GameValues.time += datetime.timedelta(seconds = 60)
        sc.fill(GameValues.BLACK)
        
        GameValues.Environment.update()
        GameValues.Clouds.update()
        PosTracEnvironment()
        GameValues.Blocks.update()
        GameValues.RedCells.update()
        
        GameValues.Blocks.draw(sc)  
        GameValues.Environment.draw(sc)
        if GameValues.activeClouds:
            GameValues.Clouds.draw(sc) 
        if not GameValues.radiationMap:
            GameValues.RedCells.draw(sc)
        if GameValues.activeGrid:
            GameValues.Grid.draw(sc)

        
        pygame.display.update()

    
