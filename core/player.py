import os
import json
import core.champion as champ

ASSETS_LOCATION = "storage/Players"


def create_dir(dir_name):
    messages = ["\tPlayer successfully created", "\tThe player with this name already exists"]
    os.chdir("storage/Players")
    print(os.getcwd())
    if not os.path.isdir(dir_name):
        print("\tThe username is available for use!")
        while True:
            try:
                age = int(input("\tInsert your age : "))
                break
            except ValueError:
                print("\tAge is supposed to be a number")

        os.makedirs(dir_name)
        os.chdir(dir_name)
        alias = open("player.json", "w+")
        data = {"name": dir_name, "age": age, "champions": []}
        alias.seek(0)
        alias.write(json.dumps(data))
        code = 0
        reset("../../..")
    else:
        code = 1
        reset("../..")
    print(messages[code])


def player_choice():
    print("\n\n\tPlayers:  ")
    choice_list = os.listdir(ASSETS_LOCATION)
    for j, player in enumerate(choice_list, 1):
        print("\t" + str(j) + ") " + player)
    print("\t" + str(len(choice_list) + 1) + ") Go back ")
    while True:
        try:
            choice = int(input("\tChoose player : ")) - 1
            if choice not in range(0, len(choice_list) + 1):
                print("Wrong number chosen.")
                continue
            break
        except ValueError:
            print("Error while choosing player.")
    if choice == len(choice_list):
        return 0
    else:
        print("\n\tWelcome " + choice_list[choice])
        return choice_list[choice]


def delete():
    players = []
    if get_player_count() != 0:
        if os.path.basename(os.getcwd()) == "Etnia":
            players = os.listdir("storage/Players")
        else:
            players = os.listdir("../../Players")
    for j, player in enumerate(players, 1):
        print("\t" + str(j) + ") " + player)
    print("\t" + str(len(players) + 1) + ") Go back ")
    while True:
        try:
            deleted = int(input("\tChoose player to delete: ")) - 1
            if deleted not in range(0, len(players) + 1):
                print("Out of bounds choice. Please choose again")
                continue
            break
        except ValueError:
            print("That's not a valid option.")

    if deleted == len(players):
        return 0
    else:
        return players[deleted]


def reset(path):
    os.chdir(path)


def play_game(name):
    os.chdir(ASSETS_LOCATION + "/" + name)
    file = open("player.json", "r+")
    data = json.loads(file.read())
    if data["name"] != name:
        import sys
        sys.exit("There's a slight mix-up. Perhaps you have move the player's file to another directory")
    while True:
        print("\n\tPLAYER : " + name)
        game_menu()
        choice = input("\n\tGAME MENU : ")
        if choice == "1":
            print("champpp")
        elif choice == "2":
            print("deletion")
        elif choice == "3":
            print("Stats")
        elif choice == "4":
            print("inventory")
        elif choice == "5":
            print("Switch")
        elif choice == "6":
            print("Battle")
        elif choice == "7":
            print(" ")
        elif choice == "8":
            print("go back")
        else:
            print("Wrong choice")
# todo : Gradually write the functions on the champion.py

def change_player():
    print(os.getcwd())
    switch_list = os.listdir(ASSETS_LOCATION)
    for j, player in enumerate(switch_list, 1):
        print("\t" + str(j) + ") " + player)
    print("\t" + str(len(switch_list) + 1) + ") Go back")
    while True:
        try:
            choice = int(input("\n\tChoose player : ")) - 1
            if choice not in range(0, len(switch_list) + 1):
                print("Wrong number chosen.")
                continue
            break
        except ValueError:
            print("Error while choosing player.")
    if choice == len(switch_list):
        return 0
    else:
        return switch_list[choice]


def get_player_count():
    return len(os.listdir(ASSETS_LOCATION))


def game_menu():
    print("\t1) Create champion")
    print("\n\t2) Delete Champion")
    print("\n\t3) Statistics")
    print("\n\t4) View inventory")
    print("\n\t5) Switch equipment")
    print("\n\t6) Free Roam Battle")
    print("\n\t7) Dungeon exploration")
    print("\n\t8) Back to main Menu")