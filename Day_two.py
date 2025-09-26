import random
# # """
# #     Python Practice Tasks
# #     =====================

# #     Rules:
# #         - Everything must be written inside functions.
# #         - The file should run as a script.
# #         - When the script starts, the user must see a menu of numbered scenarios  (1: List order, 2: Pepole with favorite color , .....).
# #         - The user chooses a number, and the program runs the corresponding function.
# #         - Each task should only run when chosen from the menu.
# #         - At ANY stage: if the user enters invalid input, the program must:
# #               * Show an error message
# #               * Display what valid input looks like
# #               * Let the user try again (do not crash or exit)

# #     Tasks:
# #     ------

# #     1 - Ask the user to enter 5 numbers.
# #         Store them, then display them in ascending order and descending order.
def list_order():
    try:
        list1 = []
        for i in range(5):
            list1.append(int(input("Enter a number:")))
    except ValueError:
        print("Invalid input please enter a number")
    list1.sort()
    print(list1)
    list1.reverse()
    print(list1)
# list_order()

# #     2 - Write a function that takes two numbers: (length, start).
# #         Generate a sequence of numbers with the given length,
# #         starting from the given start number and increasing by one each time.
# #         Print the result.
def fun_sequence(length, start):
    for i in range(length):
        print(start + i)


# fun_sequence(10, 1)

# #     3 - Keep asking the user for numbers until they type "done".
# #         When finished, print:
# #             * The total of all numbers entered
# #             * The count of valid entries
# #             * The average
# #         If the user enters something invalid, show an error and continue.
def until_done():
    total = 0
    while True:
        num = int(input("Enter a number:"))
        if num == "done":
            break
        try:
            num = int(num)
        except ValueError:
            print("Invalid input please enter a number")
            continue
        total += int(num)
    print(total)
# until_done()
# #     4 - Ask the user to enter a list of numbers.
# #         Remove any duplicates, sort the result, and display it.
def remove_duplicates():
    while True:
        try:
            user_input = input("enter your numbers:")
            nums = list(map(int, user_input.split()))
        except ValueError:
            print("plz enter a valid number")
            continue
        set1 = sorted(set(nums))
        print(set1)


# remove_duplicates()


# #     6 - Ask the user to enter a sentence.
# #         Count how many times each word appears in the sentence
# #         and display the result.
def word_freq():
    sentence = input("Enter a sentence:")
    words = sentence.strip().lower().split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print("Word frequencies:")
    for word, count in word_count.items():
        print(f"{word}: {count}")
# word_freq()        


# #     7 - Create a small gradebook system:
# #         - The user enters 5 students names and their scores.
# #         - At the end, show:
# #             * The highest score
# #             * The lowest score
# #             * The average score.
def gradebook():

    
    students = {}
    while len(students) < 5:
        name = input(f"Enter name of student {len(students)+1}/5: ").strip()
        if not name:
            print(" Name cannot be empty.")
            continue
        try:
            score = float(input(f"Enter score for {name}: "))
            students[name] = score
        except ValueError:
            print("Invalid score. Please enter a number.")
    
    scores = list(students.values())
    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.2f}")


# #     8 - Write a program that simulates a shopping cart:
# #         - The user can add items with a name and a price.
# #         - The user can remove items by name.
# #         - The user can view all items with their prices.
# #         - At the end, display the total cost.
def shopping_cart():
    cart = []
    while True:
        item = input("Enter an item: ")
        if item == "done":
            break
        cart.append(item)
    print(cart)


# #     9 - Create a number guessing game:
# #         - The program randomly selects a number between 1 and 20.
# #         - The user keeps guessing until they get it right.
# #         - After each guess, show if the guess was too high or too low.
# #         - When correct, display the number of attempts.


def number_guessing_game():
    number = random.randint(1, 20)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter a guess (1–20): "))
        except ValueError:
            print("Invalid input! Please enter a whole number between 1 and 20.")
            continue

        attempts += 1  # count every guess

        if guess == number:
            print(f"You guessed it in {attempts} attempts!")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")



    
def main():
    print("1. List order")
    print("2. Sequence of numbers")
    print("3. Total of all numbers")
    print("4. Remove duplicates")
    print("5. Word_freq")
    print("6. Gradebook")
    print("7. Shopping cart")
    print("8. Number guessing game")
    print("9. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        list_order()
    elif choice == 2:
        fun_sequence()
    elif choice == 3:
        until_done()
    elif choice == 4:
        remove_duplicates()
    elif choice == 5:
        word_freq()
    elif choice == 6:
        gradebook()
    elif choice == 7:
        shopping_cart()
    elif choice == 8:
        number_guessing_game()
    elif choice == 9:
        exit()

if __name__ == "__main__":
    main()
