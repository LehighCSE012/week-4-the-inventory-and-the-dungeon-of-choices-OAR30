"""
Week 3 coding assignment: Bob's Adventure.

This module simulates a simple text-based adventure game where the
character encounters monsters, finds potions, and navigates
based on user input.
"""
import random

inventory = []

"""Adds item to inventory"""
def acquire_item(inventory, item):
    print(f"You acquired a {item}!")
    inventory.append(item)
    return inventory

"""Displays items in inventory"""
def display_inventory(inventory):
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for count, item in enumerate(inventory, 1):
            print(f"{count}. {item}")

"""Displays Player Health"""
def display_player_status(player_health):
    print("Your current health:", player_health)

"""Determines direction player goes in"""
def handle_path_choice(player_health):
    path_choice = random.choice(["left", "right"])
    
    if path_choice == "left":
        print("You decided to head left")
        print("You encounter a friendly gnome who heals you for 10 health points.")
        return player_health + 10
    else:
        print("You decided to head right")
        print("You fall into a pit and lose 15 health points.")
        player_health -= 15
        if player_health < 0:
            player_health = 0
            print("You are barely alive!")
        return player_health

"""Player Attack Module"""
def player_attack(monster_health):
    print("You strike the monster for 15 damage!")
    return max(0, monster_health - 15)

"""Monster Attack Module"""
def monster_attack(player_health):
    if random.choice([True, False]):
        print("The monster hits you for 10 damage!")
        return max(0, player_health - 10)
    print("The monster lands a critical hit for 20 damage!")
    return max(0, player_health - 20)

"""Combat between player and monster"""
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

"""Checks for treasure"""
def check_for_treasure(has_treasure):
    if has_treasure:
        print("You found the hidden treasure! You win!")
    else:
        print("The monster did not have the treasure. You continue your journey.")

"""Player enters different dungeons and discovers different items"""
def enter_dungeon(player_health, inventory, dungeon_rooms):
    print("You found gold coins in the room.")
    
    for room in dungeon_rooms:
        print(room[0])
        if room[1]:
            acquire_item(inventory, room[1])
        if room[2] == "puzzle":
            print("You encounter a puzzle!")
            choice = input("Would you like to solve the puzzle or skip?: ")
            if choice.lower() == "solve":
                success = random.choice([True, False])
                print(room[3][0] if success else room[3][1])
                player_health += room[3][2]
                player_health = max(0, player_health)
                if player_health == 0:
                    print("You are barely alive!")
                display_inventory(inventory)
                display_player_status(player_health)
        elif room[2] == "trap":
            print("You see a potential trap!")
            choice = input("Would you like to disarm the trap or skip?: ")
            if choice.lower() == "disarm":
                success = random.choice([True, False])
                print(room[3][0] if success else room[3][1])
                player_health += room[3][2]
                player_health = max(0, player_health)
                if player_health == 0:
                    print("You are barely alive!")
                display_inventory(inventory)
                display_player_status(player_health)
        elif room[2] == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")
        display_player_status(player_health)
        display_inventory(inventory)
    
    return player_health, inventory

"""Main code function"""
def main():
    player_health = 100
    monster_health = 75
    has_treasure = random.choice([True, False])
    
    player_health = handle_path_choice(player_health)
    has_treasure = combat_encounter(player_health, monster_health, has_treasure)
    check_for_treasure(has_treasure)
    
    dungeon_rooms = [
        ("Creaky Shack", "gold coins", "trap", ("You avoided the trap!", "You triggered the trap!", -10)),
        ("Cave", "key", "puzzle", ("You solved the puzzle!", "You couldn't solve the puzzle!", -5)),
        ("Ginger Bread House", "health potion", "none", None)
    ]
    
    player_health, inventory = enter_dungeon(player_health, inventory, dungeon_rooms)

if __name__ == "__main__":
    main()
