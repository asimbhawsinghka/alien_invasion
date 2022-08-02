class GameStats():
    """Track Stats for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialise Stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion  in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialise stats that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
