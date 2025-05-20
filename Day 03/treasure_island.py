treasure_map = """
 -----     ---------  -----------     -------------- ------    -------
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 ----- ----- ------------  ------- ----- -------  --------  ---------- 
 """


def get_user_choice(prompt, options):
    while True:
        print("\n" + prompt)
        print("Choose one of the following options: " + ", ".join(options))
        choice = input("Enter your choice: ").strip().lower()
        if choice in [option.lower() for option in options]:
            print(f"You chose: {choice}")
            return choice
        else:
            print("Invalid choice. Please try again.")


def play_game():
    print(treasure_map)

    print("Welcome to the Treasure Island!")
    print("Your mission is to find the treasure.")

    message = "You are at a crossroads. Where do you want to go?"
    choices = ["left", "right"]
    user_choice = get_user_choice(message, choices)

    if user_choice == "right":
        print("You fell into a hole and were eaten by a ravenous beast.")
        print("Game Over.")
        return

    message = "You come to a lake that so dark blue you cannot see anything in it. You can swin across it or wait for a boat."
    choices = ["swim", "wait for a boat"]
    user_choice = get_user_choice(message, choices)

    if user_choice == "swim":
        print("Something grabs you leg and pulls you under. You are never seen again.")
        print("Game Over.")
        return

    message = "You arrive at a wall with three doors set into it. One red, one yellow, and one blue. Which color do you choose?"
    choices = ["red", "yellow", "blue"]
    user_choice = get_user_choice(message, choices)

    if user_choice == "red":
        print("The red door leads to a room full of fire. You are burned to a crisp.")
        print("Game Over.")
        return
    elif user_choice == "blue":
        print(
            "A pale blue arm grabs you and pulls you into the room. You are eaten by something."
        )
        print("Game Over.")
        return

    print("\nYou enter a room full of gold and jewels. You have found the treasure!")
    print("Congratulations! You win!")


if __name__ == "__main__":
    play_game()
