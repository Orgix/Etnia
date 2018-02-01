import os
import json

ASSETS_LOCATION = "storage/Players"

# TODO ADD COMMENTS ON PY SCRIPTS

print("testing")

def create_dir(dir_name):
    messages = ["\tPlayer successfully created", "\tThe player with this name already exists"]
    if not os.path.isdir(dir_name):
        print("\tThe username is avaiable for use!")

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
    print(os.getcwd())
    print(messages[code])


def player_choice():
    print("\n\n\tPlayers:  ")
    players = os.listdir(ASSETS_LOCATION)
    for j, player in enumerate(players):
        print("\t" + str(j + 1) + ") " + player)

    while True:
        try:
            choice = int(input("Choose player : ")) - 1
            if choice not in range(0, len(players)):
                print("Wrong number chosen.")
                continue
            break
        except ValueError:
            print("Error while choosing player.")
# TODO Take a good look here. It is intended that the scripts choose a player in the end so we can proceed to the menu

def delete():
    players = os.listdir(ASSETS_LOCATION)
    for j, player in enumerate(players):
        print("\t" + str(j + 1) + ") " + player)

    while True:
        try:
            deleted = int(input(" Choose player to delete: ")) - 1
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
