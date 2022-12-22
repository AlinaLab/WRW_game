"""This module should provide two functions: get_player_name and play"""

from models import Enemy, Player
from exceptions import EnemyDown, GameOver


def get_player_name() -> str:
    player_name: str = ""
    while not player_name:
        player_name = input("ENTER YOUR NAME: ").strip()
    return player_name


def play() -> None:
    player_name = get_player_name()
    player = Player(player_name)
    initial_enemy_level = 1
    enemy = Enemy(initial_enemy_level)
    print(f"Your health is {player.health}. Enemy level {enemy.health}\n")
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown as exc:
            print(exc)
            initial_enemy_level += 1
            enemy = Enemy(initial_enemy_level)
            player.increase_health()
        except GameOver as exc:
            print(exc)
            print(f"---------------------------Your score is {player.score}--------------------------")
            print(f"------------------------------GAME OVER-----------------------------")
            break


if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        pass
