from constants import * 
from circleshape import * 
import pygame 
from asteroid import Shot 


class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,(255,255,255), self.triangle(), 2)

    def rotate(self,dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.timer > 0:
            self.timer -= dt 

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt 

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)        
        shot_velocity = pygame.Vector2(0,1)
        shot_velocity = shot_velocity.rotate(self.rotation)
        shot_velocity *= PLAYER_SHOT_SPEED
        shot.velocity = shot_velocity
        self.timer = PLAYER_SHOOT_COOLDOWN
        
        