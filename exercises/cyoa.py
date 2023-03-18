"""Choose Your own Adventure Program."""

__author__ = "730476572"


ALIVE: str = "\U0001f603"
DEAD: str = "\U0001f480"


player_lives: str = ALIVE * 2
comp_lives: str = ALIVE * 2

damage_player: int = 0
damage_comp: int = 0

player: str = input("What is your name? ")

# equivalent as amount of ammo
player_points: int = 0
points_comp: int = 0


def greet() -> None:
    """Greet function to introduce the game."""
    print(f"Hi { player }, welcome to the 'Load, Shoot, Block' game.\n In each round, you will choose to load, shoot, or block, and you will go against a computer that chooses a random action.\n Both you and the computer will have 2 lives (represented by smiley face {ALIVE} and skull{DEAD}), and whoever loses both lives first loses the game.")
    print("Just like the meaning of those words, 'load' means loading an ammo; 'shoot' uses an ammo and damages the opponent; 'block' blocks a shot. The game ends in a tie if both players die at the same time.")
    print("You will also obtain the choice to deal direct damage when you have 3 or more ammos. A direct damage takes away one life and is unblockable.")
    print("Game starts.")


def computer() -> str:
   """Function representing how the computer/opponent works."""
   import random
   global points_comp, comp_lives
   comp_load: bool = False
   comp_block: bool = False
   comp_shoot: bool = False
   comp_direct: bool = False
   if (comp_lives != DEAD * 2 and player_lives != DEAD * 2): 
       # generates a random int from 1 to 3 (included): 1 is load, 2 is block, 3 is shoot
       num: int = random.randint(1, 3)
       if (num == 1):
          comp_load = True
       elif (num == 2):
          comp_block = True
       elif (num == 3 and points_comp > 0):
          comp_shoot = True
       elif (num == 3 and points_comp == 0):
          num = random.randint(1, 2)
          if (num == 1):
             comp_load = True
          elif (num == 2):
             comp_block = True
       # when computer has 3 ammos, generates a random int from 1 to 4 (included) where 4 is dealing direct damage
       if (points_comp >= 3):
          num = random.randint(1, 4)
          if (num == 1):
             comp_load = True
          if (num == 2):
             comp_block = True
          if (num == 3):
             comp_shoot = True
          if (num == 4):
             comp_direct = True
   comp_action: str = ""
   if (comp_shoot == True):
      comp_action = "shoot"
      return(comp_action)
   elif (comp_block == True):
      comp_action = "block"
      return(comp_action)
   elif (comp_direct == True):
      comp_action = "direct damage"
   else:
      comp_action = "load"
   return(comp_action)
   

def game_procedure() -> None:
    """Procedures of the game."""
    player_load: bool = False
    player_block: bool = False
    player_shoot: bool = False
    player_direct: bool = False
    comp_block: bool = False
    comp_shoot: bool = False
    comp_direct: bool = False
    global player_points, points_comp, damage_player, damage_comp, player_lives, comp_lives
    # asks the player to load, block, shoot (only when ammo/player_points > 0), or direct damage (only when player_points/ammo >= 3)
    while True:
        action: str = input(f"{player}, please choose one from the following actions: load, shoot, block, or 'direct damage'. ")
        if action == "load":
            player_load = True
            player_points += 1
            break
        elif action == "block":
            player_block = True
            break
        elif action == "shoot":
            if player_points == 0:
                print("You do not have any ammo. Please choose a different action.")
            else:
                player_shoot = True
                player_points -= 1
                break
        elif action == "direct damage":
            if player_points < 3:
                print("You do not have enough ammos for a direct damage. Please choose a different action.")
            else:
                player_direct = True
                direct_damage(player_points)
                break
        else:
            print("Please only type one of the following actions: 'load', 'shoot', 'block', or 'direct damage'. ")
    # consequence of shooting or dealing direct damage
    comp_action: str = computer()
    if (comp_action == "load"):
        points_comp += 1
    elif (comp_action == "block"):
        comp_block = True
    elif (comp_action == "shoot" and points_comp > 0):
        comp_shoot = True
        points_comp -= 1
    elif (comp_action == "direct damage"):
        comp_direct = True
        direct_damage(points_comp)
    if (player_shoot == True and comp_block == False):
        damage_comp += 1
    elif (player_shoot == True and comp_block == True):
        comp_block = False
    elif (player_direct == True):
        damage_comp += 1
    if (comp_shoot == True and player_block == False):
        damage_player += 1
    elif (comp_shoot == True and player_block == True):
        player_block = False
    elif (comp_direct == True):
       damage_player += 1
    if (damage_player == 2 or damage_comp == 2):
        player_lives = DEAD * 2
        comp_lives = DEAD * 2
    elif (damage_player == 1):
        player_lives = ALIVE + DEAD
    elif (damage_comp == 1):
        comp_lives = ALIVE + DEAD
    print(f"You have {player_points} ammo, and the computer has {points_comp} ammo.")
    print(f"You chose {action}, and the computer chose {comp_action}.")
       


def lives() -> str:
    """Shows number of lives for you and the opponent."""
    global player_lives, comp_lives
    if (damage_player == 0):
       player_lives = ALIVE * 2
    elif (damage_player == 1):
       player_lives = ALIVE + DEAD
    elif (damage_player == 2):
       player_lives = DEAD * 2
    if (damage_comp == 0):
       comp_lives = ALIVE * 2
    elif (damage_comp == 1):
       comp_lives = ALIVE + DEAD
    elif (damage_comp == 2):
       comp_lives = DEAD * 2
    lives: str = f"You now have {player_lives} remaining, and your opponent now has {comp_lives} remaining."
    return(lives)


def direct_damage(ammo: int) -> int:
    """A player can use 3 ammos to deal direct damage to the opponent and take one life from them (ignoring the block)."""
    global player_points, points_comp
    if (ammo >= 3):
       ammo -= 3
    return(ammo)


def main() -> None:
  """main function for the game."""
  greet()
  while (player_lives != DEAD * 2 and comp_lives != DEAD * 2):
     game_procedure()
     computer()
     print(lives())
     if player_lives == DEAD * 2 and comp_lives == DEAD * 2:
        print("It's a tie!")
     elif player_lives == DEAD * 2:
        print(f"Sorry {player}, you lost!")
     elif comp_lives == DEAD * 2:
        print(f"Congratulations {player}, you won!")


if __name__ == "__main__":
  main()