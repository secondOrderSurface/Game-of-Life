import pygame
import GameValues


class Square(pygame.sprite.Sprite):
    
    def __init__(self, pos, group):
        self.a = GameValues.SqS
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.a + 1, self.a + 1)) 
        self.rect = self.image.get_rect(center = pos)
        self.add(group)

            
            


