
import pygame
import turtle



wn.title("Pong by @SALIOU")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
 


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x=x+sizeBtwn
        y=y+sizeBtwn
        pygame.draw.line(surface,(255,255,255), (x,0), (x,w))
        pygame.draw.line(surface,(255,255,255), (0,y), (w,y))



def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width,rows,surface)
    pygame.display.update()








def main():
    global wdth, rows
    width= 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0), (10,10,))
    flag = True
    clock = pygame.time.Clock(1)
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)

    pass

main()