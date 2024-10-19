from circleshape import *
from constants import * 
import random 
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position, self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        rnd = random.uniform(20,50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else: 
            v1 = pygame.math.Vector2.rotate(self.velocity, rnd)
            v2 = pygame.math.Vector2.rotate(self.velocity, -rnd)
            ast1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            ast2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            ast1.velocity = v1 * 1.2
            ast2.velocity = v2 * 1.2
            self.kill()


class Shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position, self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    