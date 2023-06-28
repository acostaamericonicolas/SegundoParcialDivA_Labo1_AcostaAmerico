import pygame
from config import *

class Rival(pygame.sprite.Sprite):
    def __init__(self, image_path, size, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = random.randint(4, 9)  # Velocidad aleatoria de movimiento vertical


    def update(self):
        self.rect.y += self.speed  # Mover al Rival hacia abajo
        if self.rect.y > screen.get_height():  # Si el Rival se sale de la pantalla
            self.kill()  # Eliminar al Rival

