import pygame, random
##### PANTALLA ####
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
screen_size = (ANCHO_PANTALLA, ALTO_PANTALLA)
screen = pygame.display.set_mode(screen_size)


######## RUTAS ################
image_folder = "juego_acosta/imagenes/"
path_ruta = "./juego_acosta/imagenes/fondo.png"
path_auto = "./juego_acosta/imagenes/autorojo.png"
path_fuente = "juego_acosta/fuentes/NFS.ttf"
path_diamante = "juego_acosta/imagenes/diamante.png"
path_nitro = "juego_acosta/imagenes/nitro.png"
path_vida = "juego_acosta/imagenes/vida.png"
path_score_csv = "./juego_acosta/top.csv"

########## rutas de Sonidos #############
path_sonido_colision = "juego_acosta/sonidos/choque0.mp3"
path_sonido_diamante = "juego_acosta/sonidos/diamante.mp3"
path_sonido_inicio = "juego_acosta/sonidos/inicio.mp3"
path_sonido_inicio2 = "juego_acosta/sonidos/inicio2.mp3"
path_sonido_game_over = "juego_acosta/sonidos/game_over.mp3"
path_sonido_acelerar= "juego_acosta/sonidos/ambiente.mp3"
path_sonido_vida= "juego_acosta/sonidos/vida.mp3"

########### TAMAÑO AUTOS Y AUTO RIVAL ################
SIZE_AUTO = (60,130)
SIZE_RIVAL = (60,130)
SIZE_DIAMANTE = (20, 20)  # Tamaño del diamante (ancho y alto en píxeles)
SIZE_VIDA = (40, 40)  # Tamaño del diamante (ancho y alto en píxeles)

### VELOCIDAD AUTO ######
SPEED_AUTO = 10

######## COORDENADAS RIVAL ##################

X_MIN = 50  # Valor mínimo de coordenada X
X_MAX = screen_size[0] - 50  # Valor máximo de coordenada X
Y_MIN = -700  # Valor mínimo de coordenada Y
Y_MAX = -50  # Valor máximo de coordenada Y
FRECUENCIA_RIVALES = 100  # Aparece un nuevo RIVAL cada 60 ciclos de juego
FRECUENCIA_DIAMANTES = 100
MAX_RIVALES = 3  # Máximo 3 RIVALES en pantalla al mismo tiempo


#### RELOJ ######
clock = pygame.time.Clock()
FPS = 120

#### COLORES #####

RED = (255, 0, 0)


###### DISPLAY #####
#MARGEN = 160
MARGEN = 220
DISPLAY_TOP = 0  #arriba
DISPLAY_BOTTOM = ALTO_PANTALLA  #abajo
DISPLAY_LEFT = MARGEN   #izquierda
DISPLAY_RIGHT = ANCHO_PANTALLA-MARGEN #derecha
DISPLAY_CENTER_X = ANCHO_PANTALLA // 2   #mitad en eje x
DISPLAY_CENTER_Y = ALTO_PANTALLA // 2  #mitad en eje y
DISPLAY_MIDTOP = (DISPLAY_CENTER_X, DISPLAY_TOP)  #mitad arriba
DISPLAY_MIDBOTTOM = (DISPLAY_CENTER_X, ALTO_PANTALLA)  #mitad abajo
DISPLAY_MIDLEFT = (DISPLAY_LEFT, DISPLAY_CENTER_Y)  #mitad izquierda
DISPLAY_MIDRIGHT = (DISPLAY_RIGHT, DISPLAY_CENTER_Y)  #mitad derecha
DISPLAY_CENTER = (DISPLAY_CENTER_X, DISPLAY_CENTER_Y)  #centro

#### diamantes ### 

diamante_creation_timer = pygame.time.get_ticks()  # Tiempo actual en milisegundos
diamante_intervalos = 5000 # Intervalo de tiempo en milisegundos entre la creación de diamantes
num_diamantes_total = 20  # Número total de diamantes a crear
num_diamantes_creadas = 0  # Contador de diamantes creadas
# Asignar una posición aleatoria a la moneda dentro del área permitida
diamante_position = (random.randint(160, screen.get_width() - SIZE_DIAMANTE[0] - 160),
                             random.randint(-500, -30))  # Posición inicial arriba de la pantalla

#### vidas ### 

vida_creation_timer = pygame.time.get_ticks()  # Tiempo actual en milisegundos
vida_intervalos = 5000 # Intervalo de tiempo en milisegundos entre la creación de vidas
num_vidas_total = 20  # Número total de vidas a crear
num_vidas_creadas = 0  # Contador de vidas creadas
# Asignar una posición aleatoria a la moneda dentro del área permitida
vida_position = (random.randint(160, screen.get_width() - SIZE_VIDA[0] - 160),
                             random.randint(-500, -30))  # Posición inicial arriba de la pantalla





score = 0
vidas = 30

####### COLORES ###########
NEGRO = (0, 0, 0)