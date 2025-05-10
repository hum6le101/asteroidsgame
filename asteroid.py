from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            #spwanlogic for new asteroids
            child_radius = self.radius - ASTEROID_MIN_RADIUS
            new_velocity1 = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
            direction1 = new_velocity1.normalize()
            offset_position1 = self.position + direction1 * child_radius * 2
            new_asteroid1 = Asteroid(offset_position1.x, offset_position1.y, child_radius)
            new_asteroid1.velocity = new_velocity1
            new_velocity2 = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2
            direction2 = new_velocity2.normalize()
            offset_position2 = self.position + direction2 * child_radius * 2
            new_asteroid2 = Asteroid(offset_position2.x, offset_position2.y, child_radius)
            new_asteroid2.velocity = new_velocity2

