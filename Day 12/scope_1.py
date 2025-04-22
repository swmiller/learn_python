enemies = 1  # Global variable


def increase_enemies():
    enemies = 2  # Local variable
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()


outer_function()

# Example of use global keyword
player_health = 100  # Global variable


def reduce_health():
    global player_health
    player_health -= 10
    print(f"player_health after reduction: {player_health}")


reduce_health()
print(f"player_health outside function: {player_health}")


