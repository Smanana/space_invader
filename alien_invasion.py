import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    alien_invasion_settings = Settings()
    screen = pygame.display.set_mode(
        (alien_invasion_settings.screen_width,alien_invasion_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    ship = Ship(alien_invasion_settings, screen)
    #Make a group to store bullets in
    bullets = Group()
    
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(alien_invasion_settings, screen,ship, bullets)
        ship.update()
        gf.update_screen(alien_invasion_settings,screen,ship, bullets)

run_game()