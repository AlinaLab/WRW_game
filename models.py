import random

from exceptions import EnemyDown, GameOver
import settings


class Enemy:
    def __init__(self, level: int) -> None:
        self.level = level
        self.health = level

    def __str__(self):
        return f"--------------------Enemy level {self.level} "

    def decrease_health(self):
        self.health -= settings.DECREASE_HEALTH_POINTS
        if self.health < 1:
            raise EnemyDown(self)

    def select_attack(self):
        return random.choice(settings.VALID_CHOICES)

    def select_defence(self):
        return random.choice(settings.VALID_CHOICES)


class Player:
    def __init__(self, name: str) -> None:
        self.player_name = name
        self.health = settings.INITIAL_PLAYER_HEALTH
        self.score = 0

    def __repr__(self) -> str:
        return f"\n----------------------Player {self.player_name}"

    def decrease_health(self):
        self.health -= settings.DECREASE_HEALTH_POINTS
        if self.health < 1:
            raise GameOver(self)

    def increase_health(self):
        self.health += settings.INCREASE_HEALTH_POINTS

    def _select_fight_choice(self, msg: str):
        user_choice: int = 0
        while user_choice not in settings.VALID_CHOICES:
            try:
                user_choice = int(input(msg))
            except ValueError:
                pass
        return user_choice

    def select_attack(self):
        return self._select_fight_choice("MAKE AN ATTACK CHOICE FROM: WARRIOR - 1, ROBBER - 2, WIZARD - 3: ")


    def select_defence(self):
        return self._select_fight_choice("MAKE A DEFENCE CHOICE FROM: WARRIOR - 1, ROBBER - 2, WIZARD - 3: ")

    @staticmethod
    def fight(attack, defence) -> str:
        if attack == defence:
            return "DRAW"
        if attack - defence in settings.SUCCESSFUL_ATTACKS:
            return "WIN"
        return "LOSE"

    def attack(self, enemy: Enemy) -> None:
        attack = self.select_attack()
        defence = enemy.select_defence()
        result = self.fight(attack, defence)
        if result == "WIN":
            try:
                print(f"YOUR ATTACK IS SUCCESSFUL!\n")
                enemy.decrease_health()
            except EnemyDown:
                self.score += settings.SCORE_POINTS
                print(f"------------"
                      f"You get {settings.SCORE_POINTS} additional points! Your score is {self.score}."
                      f"------------")
                raise
        elif result == "DRAW":
            print(f"IT'S A DRAW!\n")
        elif result == "LOSE":
            print(f"YOUR ATTACK IS FAILED!\n")

    def defence(self, enemy: Enemy):
        defence = self.select_defence()
        attack = enemy.select_attack()
        result = self.fight(attack, defence)
        if result == "WIN":
            self.decrease_health()
            print(f"YOUR DEFENCE HAS BEEN BREACHED! Your health is {self.health}\n")
        elif result == "DRAW":
            print(f"IT'S A DRAW!\n")
        elif result == "LOSE":
            print(f"YOUR DEFENCE IS SUCCESSFUL!\n")
