import pygame, sys 
pygame.init()

size = (800, 500)

#crear ventana
screen = pygame.display.set_mode(size)

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
#color de fondo
screen.fill(pygame.Color("white"))
# ZONA DE DIBUJO
for x in range(100, 700, 100):
        pygame.draw.rect(screen, pygame.Color("white"), (x, 100, 50, 20))
        pygame.draw.line(screen, pygame.Color("green"), (x + 25, 0), (x + 25, 100), 5)
        

#actualizar pantalla
pygame.display.flip()


import pygame
import sys

pygame.init()

size = (800, 500)

# Crear ventana
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Color de fondo
    screen.fill(pygame.Color("white"))

    # ZONA DE DIBUJO
    for x in range(100, 700, 100):
        pygame.draw.rect(screen, pygame.Color("white"), (x, 100, 50, 20))
        pygame.draw.line(screen, pygame.Color("green"), (x + 25, 0), (x + 25, 100), 5)

    # Actualizar pantalla
    pygame.display.flip()