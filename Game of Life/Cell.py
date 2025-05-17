import pygame
import pandas as pd
import numpy as np
import GameValues
import tensorflow as tf
from itertools import product
from AbstractCl import Square

class RedCell(Square):
    
    data = pd.DataFrame(columns=[])
    
    def __init__(self, pos, group):
        super().__init__(pos, group)
        pygame.draw.rect(self.image, GameValues.RED, (0, 0, self.a, self.a))
        self.CreateColumns()
     
    def CreateColumns(self):
        columnsNames = []
        borders = [i for i in np.arange(0, 2 * GameValues.visionDistance + 1)]            
        for i in product(borders, borders):        
            for j in ["I", "W", "S", "B"]:
                columnsNames.append(j + str(i))
                
        columnsNames.append("Nutrition")
        columnsNames.append("Water")
        
        self.data = pd.DataFrame(columns = columnsNames)
        
        
    def CheckСonditions(self):
        ### Координата центра
        FindBlock = lambda x, y: (GameValues.HEIGHT // GameValues.SqS) * ((x - GameValues.SqS) // GameValues.SqS) +  ((y - GameValues.SqS)// GameValues.SqS) ###  Может нужно оптимизировать
        posRangeX = [i for i in np.arange(self.rect.x - GameValues.visionDistance * GameValues.SqS, self.rect.x + (GameValues.visionDistance + 1) * GameValues.SqS, GameValues.SqS)]
        posRangeY = [i for i in np.arange(self.rect.y - GameValues.visionDistance * GameValues.SqS, self.rect.y + (GameValues.visionDistance + 1) * GameValues.SqS, GameValues.SqS)]
        posNear = list(product(posRangeX, posRangeY))
        
        blocks = GameValues.Blocks.sprites()
        
        dataColumns = []
        for i in posNear:
            index = FindBlock(i[0], i[1])
            block = blocks[index]
            dataColumns.append(block.intensity)
            dataColumns.append(block.waterMass)
            dataColumns.append(block.intensity)
            dataColumns.append(block.let)
           
        dataColumns.append(0)
        dataColumns.append(0) 
        
        
        self.data.loc[len(self.data)] = dataColumns

        
    def update(self):
        self.CheckСonditions()
            

                
        



        
        
