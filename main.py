import shutil
import os
import core.player as player


Codes = ["NOT_READY", "READY"]
STATUS_CODE = Codes[0]
CURR_PLAYER = None


def main_menu():

    print("      --------------------------------Menu--------------------------------")
    print("\t1) Play")

    if CURR_PLAYER is None:
        print("\n\t2) Choose Player")
    else:
        print("\n\t2) Switch Player")

    print("\n\t3) Create Player")
    print("\n\t4) Delete Player")
    print("\n\t5) Quit")


def play():
    if CURR_PLAYER is not None:
        player.play_game(CURR_PLAYER)
    else:
        print("\tYou need to have chosen a player")


def create_player():
    name = input("\tChoose your alias : ")
    player.create_dir(name)
    print(os.getcwd())


def choose_player():
    global CURR_PLAYER
    curr = player.player_choice()
    if type(curr) == str:
        CURR_PLAYER = curr
    print(os.getcwd())


def switch_player():
    global CURR_PLAYER
    curr = player.change_player()
    if type(curr) == str:
        if curr == CURR_PLAYER:
            print("That's the current player")
            print(os.getcwd())
        else:
            print("\n\tWelcome " + curr)
            CURR_PLAYER = curr
    print(os.getcwd())


def delete_player():
    global CURR_PLAYER
    if player.get_player_count() != 0:
        deleted = player.delete()
        if type(deleted) == str:
            os.chdir("storage/Players")
            if deleted == CURR_PLAYER:
                CURR_PLAYER = None
            shutil.rmtree(deleted)
            os.chdir("../..")
    else:
        print("No players to delete")
        print(os.getcwd())
    print(os.getcwd())


def main():
    print("--------------------------------Welcome to Etnia-------------------------------\n\n")
    main_menu()
    print(CURR_PLAYER)
    while True:
        choice = input("\n\tMAIN MENU : ")
        if choice == '1':
            play()
        elif choice == '2':
            if CURR_PLAYER is None:
                choose_player()
            else:
                switch_player()
        elif choice == '3':
            create_player()
        elif choice == '4':
            delete_player()
        elif choice == '5':
            import sys
            sys.exit("\n\tThe END")
        else:
            print("Wrong choice")
        main_menu()


if __name__ == "__main__":
    main()
