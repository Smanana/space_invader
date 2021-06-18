import pygame

class Ship():

    def __init__(self,alien_invasion_settings,screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.alien_invasion_settings = alien_invasion_settings

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        #Movement Flag
        self.moving_right = False
        self.moving_left = False
        #self.moving_up = False

    def update(self):
        """Update the ship's position baed on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.alien_invasion_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.alien_invasion_settings.ship_speed_factor

        # if self.moving_up and self.rect.up < self.screen_rect.up:
        #     self.center += self.alien_invasion_settings.ship_speed_factor
        #Update rect object from self.center
        self.rect.centerx =self.center
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)


    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
