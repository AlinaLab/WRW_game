###############################################################################
                      WARRIORS, ROBBERS AND WIZARDS GAME
###############################################################################

Warriors, robbers and wizards (WRW) game is a "Paper, Rock and Scissors" clone,
but in a fantasy setting. It comes with a simple command line interface where
the use must type in his or her choice. The enemy is controlled by the script.
The player's goal is to gain as many score points, as it possible.

*****************
Code Organization
*****************

Use separate modules to maintain your code base. For example:

::

    /
    |-- engine.py
    |-- exceptions.py
    |-- models.py
    |-- settings.py

******************************
General Playground Description
******************************

The game process is divided into rounds. Each round consists of **attack** and
**defence** stages. Rounds are repeated, until player is defeated.

Fight Rules
===========

It's simple...

- **Warrior** beats **Robber**
- **Robber** beats **Wizard**
- **Wizard** beats **Warrior**

Attack Stage
============

Player selects the choice to attack from **warrior**, **robber** or **wizard**,
enemy selects the choice for defence from the same options by random. If the
attack is successful:

- enemy health is decreased
- player gains score points

In case enemy is defeated:

- a new enemy instance is initialized using higher level
- player gains some extra score points
- next defence stage is skipped, and player attacks again

Defence Stage
=============

Player selects the choice to defend from **warrior**, **robber** or **wizard**,
enemy selects the choice to attack from the same options by random. If the
attack is successful:

- player health is decreased

If player is defeated:

- report the message about gained score points to the terminal
- write down player's name and score points to "scores.txt" file

**********
Exceptions
**********

Enemy Down
==========

This is an exceptional scenario when enemy is defeated. A custom exception
``EnemyDown`` should be used to track these cases. Exception should provide
the details on the enemy's instance, especially its level.

Game Over
=========

This is an exceptional scenario when player is defeated. A custom exception
``GameOver`` should be used to track these cases. Exception should provide
the details on the player's instance, especially its score points.

******
Models
******

Enemy
=====

Represents the playing enemy-bot. All choices made by this model are random.
The model should implement methods:

:``__init__``:
    Initialize enemy instance. Initializer should receive one argument of
    integer type - ``level: int``. Health points value should be set equal
    to level value.

:``descrease_health``:
    Method decreases the health points value by 1 (one). If this value becomes
    less that 1 (one) the ``EnemyDown`` exception is raised.

:``select_attack``:
    Return a random attack choice from valid choices.

:``select_defence``:
    Return a random defence choice from valid choices.

You are free to implement other methods you like, if needed.

Player
======

This model is controlled by the user. It represents a playing user. All choices
are controlled by the user. The model should implement methods:

:``__init__``:
    Initialize player instance. Initializer should receive player's name as
    an argument - ``name: str``. Health points are to be set from settings.
    Score points should be initialized with 0 (zero).

:``decrease_health``:
    Method decreases the health points value by 1 (one). If this value becomes
    less that 1 (one) the ``GameOver`` exception is raised.

:``select_attack``:
    Return a fight choice made by the user. Performs choice validation.

:``select_defence``:
    Return a fight choice made by the user. Performs choice validation.

:``fight``:
    Static method to perform a fight. Takes two arguments representing attack
    and defence choices. Performs fight result calculation and return it back.

:``attack``:
    Perform attack on an enemy instance. This method takes an enemy instance as
    an argument. After that, it takes attack choice from the player model and
    the defence choice from an enemy model. After fight result calculation
    required operation are to be performed (decrease enemy health, assign
    score points etc.). Based on fight result should print out a message:

    - ``"YOUR ATTACK IS SUCCESSFUL!"``
    - ``"YOUR ATTACK IS FAILED!"``
    - ``IT'S A DRAW!"``

:``defence``:
    Perform defence from an enemy attack. This method takes an enemy instance
    as an argument. After that, it takes defence choice from the player model
    and the attack choice from an enemy model. After fight result calculation
    required operation are to be performed (decrease player health). Based on
    fight result should print out a message:

    - ``"YOUR DEFENCE IS SUCCESSFUL!"``
    - ``"YOUR DEFENCE IS FAILED!"``
    - ``IT'S A DRAW!"``

********
Settings
********

**settings.py** module contains constants values for the game (e.g.
``INITIAL_PLAYER_HEALTH = 5``).

******
Engine
******

Engine module should provide two functions:

- ``get_player_name``
- ``play``

Player name getter
==================

Asks the user to type in his or her name and return it back.
Leading and trailing whitespaces are to be trimmed.
Name should contain at least one character.

Play
====

This function initializes player and enemy instance.
It processes game rounds inside of an endless loop stage by stage.
If an enemy is defeated - a new one should be initialized with level increased
by 1 (one). This case should be reported to the terminal.
If a player is defeated - the "Game Over" message should be reported to the
terminal.
``KeyboardInterrupt`` should be handled as well - it's behavior is similar
to "Game Over" event, but "game over" message should be omitted.

*********************
Optional Enhancements
*********************

#.  Add scores processor to show top-10 scores from a record table.
#.  Create game menu, for example:
    ::

        AVAILABLE MENU CHOICES: PLAY, SCORES, EXIT
        TYPE YOUR CHOICE HERE:

