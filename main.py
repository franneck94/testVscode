def game_guide():
    print("Welcome to the guessing game. If you guess the correct number you will win!")
    print("The number range is [0, 100]")

def game_logic(goal):
    while True:
        input_number = int(input("Enter the number: "))
        if input_number > goal:
            print("The number is too big!")
        elif input_number < goal:
            print("The number is too small!")
        else:
            print("You won the game!")
            break

def main():
    goal = 45
    game_guide()
    game_logic(goal)


if __name__ == "__main__":
    main()
