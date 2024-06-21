import pygame
import random
import math
from pygame import mixer

pygame.init()  # Inicializamos a pygame
tamano_pantalla = (800, 600)

# Creamos la pantalla
pantalla = pygame.display.set_mode(tamano_pantalla)

# Configuraciones para la pantalla: Título, icono y fondo
pygame.display.set_caption("Clon espace invaders")  # Título que aparece arriba en la ventana
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)  # Icono que aparece en la ventana del juego al lado del título
fondo = pygame.image.load("fondo.jpg")

# variable jugador
img_jugador = pygame.image.load("cohete.png")
jugador_posx = 368  # 400 mitad de la pantalla, 28 porque el tamaño de la imagen es de 64px
jugador_posy = 500  # tomamos el alto y le restamos el alto de la imagen
jugador_x_cambio = 0

# variable enemigo
# img_enemigo = pygame.image.load("enemigo.png")
# enemigo_posx = random.randint(0, 736)
# enemigo_posy = random.randint(50, 200)
# enemigo_x_cambio = 0.5
# enemigo_y_cambio = 50.0
img_enemigo = []
enemigo_posx = []
enemigo_posy = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_posx.append(random.randint(0, 736))
    enemigo_posy.append(random.randint(50, 200))
    enemigo_x_cambio.append(1.5)
    enemigo_y_cambio.append(50)

# variable bala
img_bala = pygame.image.load("bala.png")
balas = []  # listan para manejar multiples balas

# Variable puntaje
puntaje = 0
fuente = pygame.font.Font("Jacquard12-Regular.ttf", 32)
texto_x = 10
texto_y = 10

# agregar musica
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)  # se repite cada vez que termine


# mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Disparar bala
def disparar_bala(x, y):
    balas.append([x, y])


# Detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    # https://trilosangulo.blogspot.com/2021/09/calcular-la-distancia-entre-dos-puntos.html
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    return distancia < 27


# texto final de juego
fuente_final = pygame.font.Font("CFBogswaDemo-SemiBold.otf", 50)


def texto_final():
    mi_fuente_final = fuente_final.render("PERDISTE... JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (30, 200))  # centro de la pantalla


# Loop del juego
se_ejecuta = True
while se_ejecuta:

    # pantalla.fill((25, 144, 228))  # Color de fondo de la pantalla
    pantalla.blit(fondo, (0, 0))

    # Iterar eventos
    for evento in pygame.event.get():  # Escuchamos las entradas del usuario
        # evento cerrar
        if evento.type == pygame.QUIT:  # Sí hizo clic en la X para cerrar la ventana de juego
            se_ejecuta = False

        # evento presionar teclas
        if evento.type == pygame.KEYDOWN:  # se fija si se presiono una tecla
            if evento.key == pygame.K_LEFT:  # se fija si se presiono la fecla izquierda presionada
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:  # se fija si se presiono la fecla izquierda presionada
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:  # Disparamos
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                disparar_bala(jugador_posx, jugador_posy)

        # evento soltar flechas
        if evento.type == pygame.KEYUP:  # se fija se solto una tecla
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # modificar ubicacion de la nave (jugador)
    jugador_posx += jugador_x_cambio  # actualizamos la variable para que el jugador se mueva

    # mantener la nave dentro de la pantalla (jugador)
    if jugador_posx <= 0:  # límite para la izquierda
        jugador_posx = 0
    elif jugador_posx >= 736:  # límite para la derecha
        jugador_posx = 736

    # modificar ubicacion de la nave (enemigo)
    for e in range(cantidad_enemigos):
        # Fin del juego
        if enemigo_posy[e] > 500:  # si algún enemigo alcanzo la altura de la nave del jugador
            for k in range(cantidad_enemigos):
                enemigo_posy[k] = 1000  # sacamos a los enemigos de la pantalla
            texto_final()
            break

        enemigo_posx[e] += enemigo_x_cambio[e]  # actualizamos la variable para que el enemigo se mueva

        # mantener las naves enemigas dentro de la pantalla
        if enemigo_posx[e] <= 0:  # límite para la izquierda
            enemigo_x_cambio[e] = 1  # cambia el movimiento a la derecha
            enemigo_posy[e] += enemigo_y_cambio[e]  # hace que baje la nave enemiga
        elif enemigo_posx[e] >= 736:  # límite para la derecha
            enemigo_x_cambio[e] = -1  # cambia el movimiento a la izquierda
            enemigo_posy[e] += enemigo_y_cambio[e]  # hace que baje la nave enemiga

        # verificar colision
        for bala in balas:
            colision = hay_colision(enemigo_posx[e], enemigo_posy[e], bala[0], bala[1])
            if colision:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_posx[e] = random.randint(0, 736)
                enemigo_posy[e] = random.randint(50, 200)

        enemigo(enemigo_posx[e], enemigo_posy[e], e)  # pintamos el enemigo

    # Actualizar la posicion de cada bala y eliminar las que salen de la pantalla
    # balas = [[x, y - 3] for x, y in balas if y > -64]
    balas_actualizadas = []
    for bala in balas:
        bala[1] -= 3  # la bala sube
        if bala[1] > -64:  # si la bala está dentro de la pantalla se añade a balas_actualizdas
            balas_actualizadas.append(bala)
    balas = balas_actualizadas

    for bala in balas:
        pantalla.blit(img_bala, (bala[0] + 16, bala[1] + 10))

    jugador(jugador_posx, jugador_posy)  # pintamos el jugador
    mostrar_puntaje(texto_x, texto_y)
    # actualizar
    pygame.display.update()  # Actualizamos la pantalla
