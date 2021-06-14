import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    alien_invasion_settings = Settings()
    screen = pygame.display.set_mode(
        (alien_invasion_settings.screen_width,alien_invasion_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    ship = Ship(alien_invasion_settings, screen)
    
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(alien_invasion_settings,screen,ship)

run_game()