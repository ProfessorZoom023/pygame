import pygame,os
WIDTH, HEIGHT=1000,700
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("spaceship wars")
color=(100,100,250)
sw,sh=(70,70)
yspc=pygame.image.load('spaceship wars\spaceship_yellow.png')
yspc=pygame.transform.rotate(pygame.transform.scale(yspc,(sw,sh)),90)
rspc=pygame.image.load('spaceship wars\spaceship_red.png')
rspc=pygame.transform.rotate(pygame.transform.scale(rspc,(sw,sh)),270)


FPS=60
def display(red,yellow):
     win.fill(color)
     win.blit(yspc,(yellow.x, yellow.y))
     win.blit(rspc,(red.x, red.y))
     pygame.display.update()

def main():
    red=pygame.Rect(100,350,sw,sh)
    yellow=pygame.Rect(400,300,sw,sh)
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        red.x+=1
        display()
       
        

    pygame.quit()

if __name__ =="__main__":
    main()


