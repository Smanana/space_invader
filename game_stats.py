class GameStats():
    """Track statistics for Alien Invasion."""
    def __init__(self, alien_invasion_settings):
        """Initialize statistics."""
        self.alien_invasion_settings = alien_invasion_settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = True


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.alien_invasion_settings.ship_limit