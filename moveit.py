import os, pygame, sys

main_dir = os.path.split(os.path.abspath(__file__))[0]

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > 600:
            self.pos.left = 0

def load_image(name):
    path = os.path.join(main_dir, "data", name)
    return pygame.image.load(path).convert()

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    player = load_image('player.gif')
    background = load_image('liquid.bmp')
    background = pygame.transform.scale2x(background)
    background = pygame.transform.scale2x(background)

    screen.blit(background, (0, 0))

    objects = []
    for x in range(10):
        o = GameObject(player, x*40, x)
        objects.append(o)

    while 1:
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.KEYDOWN):
                sys.exit()

        for o in objects:
            screen.blit(background, o.pos, o.pos)
        for o in objects:
            o.move()
            screen.blit(o.image, o.pos)

        pygame.display.update()
        pygame.time.delay(100)
    # move_and_draw_all_game_objects()
        
if __name__ == "__main__":
    main()
    pygame.quit()