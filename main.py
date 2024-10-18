import pygame
from constants import * 
from player import * 
from asteroid import * 
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers=(asteroids, updatable, drawable)
    AsteroidField.containers= (updatable)
    



    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()
    

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for p in updatable:
            p.update(dt)
        # player.update(dt)
        for p in drawable:
            p.draw(screen)
        pygame.display.flip()        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()