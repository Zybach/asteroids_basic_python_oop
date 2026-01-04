import sys
import pygame
import constants
from logger import log_state
from logger import log_event
import player
import asteroid
import asteroidfield
import shot


def main():
    print("Starting Asteroids with pygame version:" + pygame.version.ver)
    print("Screen width: " + str(constants.SCREEN_WIDTH))
    print("Screen height: " + str(constants.SCREEN_HEIGHT))
    
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    shot.Shot.containers = (updatable, drawable, shots)
    asteroidfield.AsteroidField.containers = (updatable)
    
    field = asteroidfield.AsteroidField()
    
    starship = player.Player(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2, constants.PLAYER_RADIUS)
    
    dt = 0
    
    
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        updatable.update(dt)
        if starship.shotcooldown > 0:
            starship.shotcooldown -= dt
            if starship.shotcooldown < 0:
                starship.shotcooldown = 0
        
        for ast in asteroids:
            for sh in shots:
                if ast.collides_with(sh):
                    log_event("asteroid_shot")
                    ast.split()
                    sh.kill()
            if starship.collides_with(ast):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        
        for thing in drawable:
            thing.draw(screen)
        
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        print(f"Delta time {dt}")
        
    


if __name__ == "__main__":
    main()
