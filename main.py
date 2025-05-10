# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from score import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # name the Gamewindow
    pygame.display.set_caption("Asteroids: The Game")

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    score = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers=(updatable,)
    Shot.containers=(updatable, drawable, shots)
    Score.containers=(drawable,)

    asteroidfield = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    score = Score()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        screen.fill("black")



        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                exit()
            for other_asteroid in asteroids:
                if other_asteroid == asteroid:
                    pass
                else:
                    if asteroid.collision(other_asteroid):
                        asteroid.split()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                    score.score_increment()

        for dr in drawable:
            dr.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
