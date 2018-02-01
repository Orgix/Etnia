import os
import json


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
        alias = open("player.json","w+")
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
    i=1
    players = os.listdir("Assets/Players")
    players = players[:len(players)-2]
    for player in players:
        print("\t" + str(i) +") "+player)
        i += 1


def delete():
    players = os.listdir("Assets/Players")
    players = players[:len(players) - 2]
    j = 1

    for player in players:
        print("\t" + str(j) + ") " + player)
        j += 1

    while True:
        try:
            deleted = int(input(" Choose player to delete: ")) - 1
            break
        except ValueError:
            print("That's not a valid option.")

    import shutil
    deleted = players[deleted]
    os.chdir("Assets/Players")
    shutil.rmtree(deleted)

    print("Player was removed from list")
    reset("../..")


def reset(path):
    os.chdir(path)
