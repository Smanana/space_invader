import sys
import pygame
from bullet import Bullet


def check_keydown_events(event,alien_invasion_settings,screen,ship,bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True  
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(alien_invasion_settings, screen, ship, bullets)


def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
  
                

def check_events(alien_invasion_settings,screen, ship, bullets):
    """Respond to keypresses and mouse"""
    for event in pygame.event.get():
        if event.type == pygame.K_q:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
          check_keydown_events(event,alien_invasion_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(alien_invasion_settings,screen, ship, alien, bullets):
    """Update images on the screen and flip t the new screen"""
    #Redraw the screen during each pass through the loop
    screen.fill(alien_invasion_settings.bg_color)
    #Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    bullets.update()

    #Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(alien_invasion_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached."""
    #Create a new bullet and add it to the bullets group
    if len(bullets) < alien_invasion_settings.bullets_allowed:
        new_bullet = Bullet(alien_invasion_settings, screen, ship)
        bullets.add(new_bullet)