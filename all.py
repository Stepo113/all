import pygame

pygame.init()
clock = pygame.time.Clock()
back = (40,154,255)
mw = pygame.display.set_mode((500,500))
game = True
class Area() :

    def __init__(self,x=0,y=0,width=10,height=10,color=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color= back
        if color:
            self.fill_color = color

    def color(self,new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw,self.fill_color,self.rect)

    def collidepoint(self,x,y):
        return self.rect.colidepoint(x,y)
    
    def colliderect(self,rect):
        return self.rect.coliderect(rect)

class Picture(Area):
    def __init__(self,filename,x=0,y=0,width=10,height=10):
        Area.__init__(self,x=x,y=y,width=width,height=height,color=None)
        self.image = pygame.image.load(filename)


    def draw(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

ball = Picture('',160,200,50,50)
platform = Picture('',200,330,100,30)
bricks = []
for j in range (3):
    y = 5 + (55 * j)
    x = 5 + (27.5 * j)
    for i in range(count):
        br = Picture('',x,y,50,50)
        bricks.append(br)
        x += 55
    count -= 1
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    mw.fill(back)
    pygame.display.update()

