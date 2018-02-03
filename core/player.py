import os
import json

ASSETS_LOCATION = "storage/Players"


def create_dir(dir_name):
    messages = ["\tPlayer successfully created", "\tThe player with this name already exists"]
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
    else:
        code = 1
    reset("../../..")
    print(messages[code])


def player_choice():
    print("\n\n\tPlayers:  ")
    players = os.listdir(ASSETS_LOCATION)
    for j, player in enumerate(players, 1):
        print("\t" + str(j) + ") " + player)
    print("\t" + str(len(players) + 1) + ") Go back ")
    while True:
        try:
            choice = int(input("\tChoose player : ")) - 1
            if choice not in range(0, len(players) + 1):
                print("Wrong number chosen.")
                continue
            break
        except ValueError:
            print("Error while choosing player.")
    if choice == len(players):
        return 0
    else:
        print("Welcome " + players[choice])
        return players[choice]


def delete():
    players = os.listdir(ASSETS_LOCATION)
    for j, player in enumerate(players, 1):
        print("\t" + str(j) + ") " + player)

    while True:
        try:
            deleted = int(input("\tChoose player to delete: ")) - 1
            if deleted not in range(0, len(players)):
                print("Out of bounds choice. Please choose again")
                continue
            break
        except ValueError:
            print("That's not a valid option.")

    import shutil
    deleted = players[deleted]
    os.chdir("storage/Players")
    shutil.rmtree(deleted)

    print("Player was removed from list")
    reset("../..")


def reset(path):
    os.chdir(path)


def play_game():
    file = open("player.json", "r+")
    data = json.loads(file.read())
    game_menu()
    while True:
        print("kappa")
        game_menu()
        break


def game_menu():
    print("\t1) Create champion\n\t2) Delete Champion\n\t"
          "3) Statistics\n\t4) View inventory\n\t5) Switch equipment\n\t"
          "6) Free Roam Battle\n\t7) Dungeon exploration\n\t8) Switch player")