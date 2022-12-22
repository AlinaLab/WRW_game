"""
Module of Enemy Down and Game Over.

Enemy Down: This is an exceptional scenario when enemy is defeated.
A custom exception EnemyDown should be used to track these cases.
Exception should provide the details on the enemy's instance, especially its level.

Game Over: This is an exceptional scenario when player is defeated.
A custom exception GameOver should be used to track these cases.
Exception should provide the details on the player's instance, especially its score points.

"""


class _AbstractModelException(Exception):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj

    def __str__(self):
        return f"{self.obj} is defeated.----------------------\n"

class EnemyDown(_AbstractModelException):
    """This is an exceptional scenario when enemy is defeated"""


class GameOver(_AbstractModelException):
    """This is an exceptional scenario when player is defeated"""


