import pygame
from settings import Settings
from ship import Ship
from alien import Alien
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
    aliens = Group()
    
    #Create the fleet of aliens.
    gf.create_fleet(alien_invasion_settings, ship, screen, aliens)
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(alien_invasion_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(alien_invasion_settings,aliens)
        gf.update_screen(alien_invasion_settings,screen,ship, aliens, bullets)
        

run_game()