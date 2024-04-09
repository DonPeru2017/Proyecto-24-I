import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana del juego
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))

# Cargar la imagen del logo del juego
try:
    logo = pygame.image.load('logo.png')
    logo = pygame.transform.scale(logo, (ancho, alto)) 
except pygame.error:
    print("No se pudo cargar la imagen 'logo.png'. Asegúrate de que el archivo esté en el mismo directorio que tu script de Python.")
    sys.exit()

# Función para dibujar el logo en el centro de la pantalla
def dibujar_logo():
    ventana.blit(logo, (0, 0)) 

# Función para dibujar el botón de jugar
def dibujar_boton():
    boton = pygame.Rect(350, 450, 100, 50)  # Crear un rectángulo para el botón
    pygame.draw.rect(ventana, [0, 255, 0], boton)  # Dibujar el botón

    fuente = pygame.font.Font(None, 24)  # Crear una fuente
    etiqueta = fuente.render("Jugar", 1, (255, 255, 255))  # Crear una etiqueta con la fuente
    ventana.blit(etiqueta, (375, 465))  # Dibujar la etiqueta en el botón

# Función para la segunda pantalla
def segunda_pantalla():
    ventana.fill((0, 0, 0))  # Rellenar la pantalla con color negro
    fuente = pygame.font.Font(None, 24)  # Crear una fuente
    etiqueta = fuente.render("Segunda pantalla", 1, (255, 255, 255))  # Crear una etiqueta con la fuente
    ventana.blit(etiqueta, (375, 300))  # Dibujar la etiqueta en el centro de la pantalla

# Bucle principal del juego
pantalla_inicio = True
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if pantalla_inicio and 350 <= pygame.mouse.get_pos()[0] <= 450 and 450 <= pygame.mouse.get_pos()[1] <= 500:
                pantalla_inicio = False

    if pantalla_inicio:
        # Rellenar la pantalla con color
        ventana.fill((0, 0, 0))

        # Dibujar el logo
        dibujar_logo()

        # Dibujar el botón de jugar
        dibujar_boton()
    else:
        # Mostrar la segunda pantalla
        segunda_pantalla()

    # Actualizar la pantalla
    pygame.display.flip()