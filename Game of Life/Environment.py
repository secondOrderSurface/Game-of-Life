import pygame 
import random
import GameValues
from numpy import reshape, array, arange
from math import dist
from AbstractCl import Square


class Sun(pygame.sprite.Sprite):
    
    intensity = 0
    
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1,1))
        self.rect = self.image.get_rect(center = (0,0))
        self.add(group)

    def CalculateIntensity(self, x):
        return ((-1/1866240) * x ** 2 + (5/108) * x)
    
    def update(self):
        secondsFromZero = 3600 * GameValues.time.hour + 60 * GameValues.time.minute + GameValues.time.second
        self.intensity = self.CalculateIntensity(secondsFromZero)

class Cloud(Square):
    
    color = GameValues.SKY
    alpha = 180
    moveCheck = 0
    rainIntensity = 0
    
    
    def __init__(self, pos, speed ,group):
        super().__init__(pos, group)
        self.image.set_alpha(self.alpha)        
        pygame.draw.rect(self.image, self.color, (0, 0, GameValues.SqS, GameValues.SqS))
        self.speed = speed
      
    def RainControl(self):  
        if (random.randint(0, GameValues.chanceRain) == 0) and (self.rainIntensity == 0):
            self.rainIntensity = random.randint(GameValues.averageRainIntensity - 3 * GameValues.standardDeviationRain, 
                                                GameValues.averageRainIntensity + 3 * GameValues.standardDeviationRain)
            
        if (random.randint(0, GameValues.chanceStopRain) == 0) and (self.rainIntensity != 0):
            self.rainIntensity = 0
            
  
    def update(self):
        self.RainControl()
        if self.moveCheck <= GameValues.SqS:
            self.moveCheck += self.speed
        else:
            self.rect.x += GameValues.SqS
            self.moveCheck = 0
        
        if self.rect.x > (GameValues.WIDTH - GameValues.SqS):
            self.rect.x = 1


        
### Мировое солнце   
sun = Sun(GameValues.Environment)

class Block(Square):
    color = GameValues.BLACK
    waterMass = 0
    intensity = 0
    coverByClouds = False
    let = 0
     
    def __init__(self, pos, group):
        super().__init__(pos, group)


    def SetLet(self, let):
        self.let = let
        if let:
            self.color = GameValues.ROCK
    
    def update(self):
        self.intensity = (sun.intensity  *  0.5) if self.coverByClouds else sun.intensity 
        
        if (self.waterMass != 0):
            self.waterMass -= GameValues.evaporationRate
            self.waterMass = max(0, self.waterMass)
        
        if not GameValues.radiationMap:
            if (self.let == False):
                self.color =  (0, 0, (255 / GameValues.maxWater) * self.waterMass)
            pygame.draw.rect(self.image, self.color, (0, 0, self.a, self.a))
        else:
            pygame.draw.rect(self.image, (255/1000 * self.intensity, 0, 0), (0, 0, self.a, self.a))
        
        
### Пусть яркость клетки с водой зависит от массы воды в ней     
class Water(Square):
    
    def __init__(self, pos, group):
        super().__init__(pos, group)
        pygame.draw.rect(self.image, GameValues.BLUE, (0, 0, self.a, self.a))
   
def GenerateEnvironment():
    for i in array(GameValues.GridPos).reshape((len(GameValues.GridPos) * len(GameValues.GridPos[0]), 2)):
        block = Block(i, GameValues.Blocks)
        if random.randint(0, GameValues.frequencyLet) == 0:
            block.SetLet(1)
        if random.randint(0, GameValues.frequencyClouds) == 0:
            cloud = Cloud(i, GameValues.speedOfClouds , GameValues.Clouds)
            

          
def PosTracEnvironment():
    
    blocks = GameValues.Blocks.sprites() ### Может возможно оптимизировать
    
    for block in blocks:
        block.coverByClouds = False
    
    for cloud in GameValues.Clouds:
        index = (GameValues.HEIGHT // GameValues.SqS) * (cloud.rect.x // GameValues.SqS) +  (cloud.rect.y // GameValues.SqS)
        blocks[index].coverByClouds = True
        if (blocks[index].let == False):     
            blocks[index].waterMass += cloud.rainIntensity ### Не добавляю воду, если блок с препятствиями
            blocks[index].waterMass = min(GameValues.maxWater, blocks[index].waterMass)
        
    

            
            
            


