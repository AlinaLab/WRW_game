"""Module contains constants values for the game"""

INITIAL_PLAYER_HEALTH = 3

INITIAL_ENEMY_LEVEL = 1
STEP_LEVEL = 1

INCREASE_HEALTH_POINTS = 1
DECREASE_HEALTH_POINTS = 1
SCORE_POINTS = 3              # If the player's attack is successful, player gains score points.

WARRIOR = 1
ROBBER = 2
WIZARD = 3
VALID_CHOICES = WARRIOR, ROBBER, WIZARD
SUCCESSFUL_ATTACKS = WARRIOR - ROBBER, ROBBER - WIZARD, WIZARD - WARRIOR
