import pygame
import constants
import circleshape
from logger import log_event
import random

class Asteroid(circleshape.CircleShape):
    
    position = 0
    
    
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        smaller_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - constants.ASTEROID_MIN_RADIUS)
        smaller_asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2
        smaller_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - constants.ASTEROID_MIN_RADIUS)
        smaller_asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2