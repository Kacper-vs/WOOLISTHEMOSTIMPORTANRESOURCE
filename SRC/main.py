from speech import story
import pygame as pyg 
import sys 


pyg.init()

screen = pyg.display.set_mode((800,600))
pyg.display.set_caption("WOOLISTHEMOSTIMPORTANTRESOURCE")

WHITE = (255,255,255)

running = True 

clock = pyg.time.Clock()

while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False 

    screen.fill(WHITE)
    pyg.display.flip()
    clock.tick(60)
pyg.quit()
sys.exit()
