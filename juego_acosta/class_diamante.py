import pygame, random
from config import *

diamantes_group = pygame.sprite.Group()

class Diamante(pygame.sprite.Sprite):
    def __init__(self, image_path, size, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = posicion
        self.speed = random.randint(2,3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > screen.get_width():
            self.kill()

diamantes_group = pygame.sprite.Group()

def crear_diamante():
    global diamante_creation_timer
    global num_diamantes_creadas
    # Código para crear y agregar diamantes al grupo

    if num_diamantes_creadas < num_diamantes_total:
        current_time = pygame.time.get_ticks()
        if current_time - diamante_creation_timer >= diamante_intervalos:
            # Asignar una posición aleatoria al diamante dentro del área permitida
            diamante_position = (random.randint(220, screen.get_width() - SIZE_DIAMANTE[0] - 220), random.randint(-500, -30))  # Posición inicial arriba de la pantalla

            # Crear una instancia de la clase diamante con la imagen cargada, tamaño y posición
            diamante = Diamante(path_diamante, SIZE_DIAMANTE, diamante_position)

            # Agregar la diamante al grupo diamantes_group
            diamantes_group.add(diamante)

            num_diamantes_creadas += 1
            diamante_creation_timer = current_time