import pygame, random
from config import *

vidas_group = pygame.sprite.Group()

class Vida(pygame.sprite.Sprite):
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

vidas_group = pygame.sprite.Group()

def crear_vida():
    global vida_creation_timer
    global num_vidas_creadas
    # Código para crear y agregar vidas al grupo

    if num_vidas_creadas < num_vidas_total:
        current_time = pygame.time.get_ticks()
        if current_time - vida_creation_timer >= vida_intervalos:
            # Asignar una posición aleatoria al vida dentro del área permitida
            vida_position = (random.randint(220, screen.get_width() - SIZE_VIDA[0] - 220), random.randint(-500, -30))  # Posición inicial arriba de la pantalla

            # Crear una instancia de la clase vida con la imagen cargada, tamaño y posición
            vida = Vida(path_vida, SIZE_VIDA, vida_position)

            # Agregar la vida al grupo vidas_group
            vidas_group.add(vida)

            num_vidas_creadas += 1
            vida_creation_timer = current_time