import random
import os
import core.player as player

CODE = 0


def main_menu():
    print("      --------------------------------Menu--------------------------------")
    print("\t1) Play\n\t2) Choose Player\n\t3) Create Player\n\t4) Delete Player\n\t5) Quit")


def play():
    print("haha loser")


def create_player():
    os.chdir("storage/Players")
    name = input("\tChoose your alias : ")
    player.create_dir(name)


def choose_player():
    player.player_choice()


def delete_player():
    player.delete()


def main():
    print("--------------------------------Welcome to Etnia-------------------------------\n\n")
    Mainloop = True
    main_menu()

    while Mainloop:
        choice = input("\n\tWHAT'S YOUR NEXT ACTION : ")
        if choice == '1':
            play()
        elif choice == '2':
            choose_player()
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
