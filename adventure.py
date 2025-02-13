'''
Week 3 coding assignment: Bob's Adventure.

This module simulates a simple text-based adventure game where the
character encounters monsters, finds potions, and navigates
based on user input.
'''
import random

"""" 
Displays Player Health

    Parameters: player_health (int) - The current health of the player.

    Functionality: Prints the player's current health to the console in a user-friendly format.
    For example: "Your current health: 100".

    Returns: Nothing.
"""
def display_player_status(player_health):
    print("Your current health:", player_health)
""""Determines direction player goes in"""
def handle_path_choice(player_health):
    path_choice = random.choice(["left", "right"])

    if path_choice == "left":
        print("You decided to head left")
        print("You encounter a friendly gnome who heals you for 10 health points.")
        player_health += 10
        updated_player_health = player_health
        return updated_player_health
    else:
        print("You decided to head right")
        print("You fall into a pit and lose 15 health points.")
        player_health -= 15
        if player_health < 0:
            player_health = 0
            print("You are barely alive!")
            updated_player_health = player_health
            return updated_player_health
        return updated_player_health
""""Player Attack Module"""
def player_attack(monster_health):
    monster_health -= 15
    print("You strike the monster for 15 damage!")
    updated_monster_health = int(monster_health)
    return updated_monster_health
""""Monster Attack Module"""
def monster_attack(player_health):
    result = random.choice([True, False])
    if result:
        player_health -= 10
        print("The monster hits you for 10 damage!")
        updated_player_health = int(player_health)
        return updated_player_health
    print("The monster lands a critical hit for 20 damage!")
    player_health -= 20
    updated_player_health = int(player_health)
    return updated_player_health
""""Combat between player and monster"""        
def combat_encounter(player_health, monster_health, has_treasure):
    while player_health > 0 and monster_health > 0:
        monster_health = player_attack(monster_health)
        if monster_health <= 0: 
            print("You defeated the monster")
            break
        player_health = monster_attack(player_health)
        if player_health <= 0:
            print("Game Over!")
            has_treasure = False
            break
        display_player_status(player_health)
    return has_treasure
""""Checks for treasure"""
def check_for_treasure(has_treasure):
    if has_treasure == False:
        print("The monster did not have the treasure. You continue your journey.")
    else:
        print("You found the hidden treasure! You win!")
        
""""Main code function"""
def main():
    player_health_initial = 100
    monster_health_initial = 75
    has_treasure = False
    
    has_treasure = random.choice([True, False])

    current_player_health = handle_path_choice(player_health_initial) # Using player_health_initial

    treasure_obtained_in_combat = combat_encounter(current_player_health, monster_health_initial, has_treasure) # Using monster_health_initial

    check_for_treasure(treasure_obtained_in_combat) # Or has_treasure, depending on logic
if __name__ == "__main__":
    main()