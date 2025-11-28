import pygame
import math

import numpy as np

size=28
# Initialize pygame
def run(AI):
    pygame.init()

    # Square size
    SQUARE_SIZE = 10
    # Window size
    WIDTH, HEIGHT = size*SQUARE_SIZE, size*SQUARE_SIZE
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Click to Draw Square")

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    store = [[0]*size for _ in range(size)]
    radius = 1
    BrushShape = lambda x: x**2


    def redraw():
       
        screen.fill(BLACK)
        for i in range(0, len(store)):
            for j in range(0, len(store)):
                rect = pygame.Rect(i*SQUARE_SIZE - SQUARE_SIZE // 2, j*SQUARE_SIZE - SQUARE_SIZE // 2, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, (store[i][j], store[i][j], store[i][j]), rect)

    drawing = False
    running = True
    while running:
        for event in pygame.event.get():
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    store = [[0]*size for _ in range(size)]
                    redraw()
            if event.type == pygame.QUIT:  # Window close button
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.MOUSEMOTION and drawing):  # Mouse click
                drawing = True
                xx, yy = event.pos  # Get click position
                x, y = xx//SQUARE_SIZE, yy//SQUARE_SIZE
                #store[x][y] = 255
                for i in range(x-radius, x+radius+1):
                    for j in range(y-radius, y+radius+1):
                        if min(i, j) >= 0 and max(i, j) < len(store):
                            a = (i*SQUARE_SIZE-xx)**2
                            b = (j*SQUARE_SIZE-yy)**2
                            #print("(i*SQUARE_SIZE-xx)**2 = ", a)
                            #print("(j*SQUARE_SIZE-yy)**2 = ", b)
                            #print()
                            mx = BrushShape((radius*SQUARE_SIZE))
                            #a = min(a, mx)
                            #b = min(b, mx)
                            dis = BrushShape(math.sqrt(a+b))
                            mx = (radius*SQUARE_SIZE)**2
                            dis = min(dis, mx)
                            color = (dis*255)//mx
                            color = 255-color
                            store[i][j] = max(store[i][j], color)
                x, y = x*SQUARE_SIZE, y*SQUARE_SIZE
                # Draw square centered on click
                redraw()
                #rect = pygame.Rect(x - SQUARE_SIZE // 2, y - SQUARE_SIZE // 2, SQUARE_SIZE, SQUARE_SIZE)
                #pygame.draw.rect(screen, WHITE, rect)
            elif event.type == pygame.MOUSEBUTTONUP:  # Mouse button released
                drawing = False 
                prediction = AI([[j/255 for j in i] for i in store])
                print("Predicted digit:", prediction)
       
        # Update display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
