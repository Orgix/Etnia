import os
import core.player as player

Codes = ["NOT_READY", "READY"]
STATUS_CODE = Codes[0]
print("still testing")


def main_menu():
    print("      --------------------------------Menu--------------------------------")
    # TODO Change function structure. In case a player has been chosen , the  "Choose player" appears. If not, " Choose player" appears"
    print("\t1) Play\n\t2) Choose Player\n\t3) Create Player\n\t4) Delete Player\n\t5) Quit")


def play():
    global STATUS_CODE
    if STATUS_CODE == Codes[1]:
        player.play_game()
    else:
        print("You need to have chosen a player")


def create_player():
    os.chdir("storage/Players")
    name = input("\tChoose your alias : ")
    player.create_dir(name)


def choose_player():
    curr = player.player_choice()
    if type(curr) == str:
        os.chdir("storage/Players/" + curr)
        return 1


def delete_player():
    player.delete()


def main():
    print("--------------------------------Welcome to Etnia-------------------------------\n\n")
    main_menu()
    global STATUS_CODE
    while True:
        choice = input("\n\tMAIN MENU : ")
        if choice == '1':
            play()
        elif choice == '2':
            if STATUS_CODE == Codes[0]:
                result = choose_player()
                if result == 1:
                    STATUS_CODE = Codes[1]
            else:
                print("\n\tA player has already been chosen")
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
