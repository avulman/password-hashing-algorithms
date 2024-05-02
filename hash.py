EXIT_STATEMENTS = ["Q", "QUIT", "EXIT"]
HASHING_ALGORITHMS = ["MD5", "SHA-1", "SHA-2", "NTLM", "LANMAN"]

def print_intro():
    print("Welcome to the password hashing program!\n"
        "This program showcases 5 common hashing\n"
        "algorithms including: MD5, SHA-1, SHA-2,\n"
        "NTLM, and LANMAN.\n")

def explain_algorithm():
    print("\nYou selected: (1) What is a hashing algorithm?\n")
    #time.sleep(1)
    print("Hashing is a one-way function to scramble data — it takes\n"
        "readable text and transforms it into a completely different\n"
        "string of characters with a set length. However, unlike other\n"
        "encryption algorithms that transform data, hashing is nearly \n"
        "impossible to revert.\n")
    #time.sleep(2)

def invalid_selection():
    print("Invalid selection. Try again or enter 'Q' to quit.")

def learn_more(selected_algorithm):
    print("Learn more about the", selected_algorithm + ".\n")

def selected_statement(option):
    print("\nYou have selected *", option, "*\n")

def select_algorithm():
    while True:
        option = input("Enter an algorithm to learn more or 'Q' to quit:\n").upper()
        if option in EXIT_STATEMENTS:
            print("Quitting... See you next time!")
            sys.exit(0)
        elif option in HASHING_ALGORITHMS:
            selected_statement(option)
            return option
        else:
            invalid_selection()

def select_main_features(selected_algorithm):
    option_1_selected = False
    option_2_selected = False
    while True:
        if not option_1_selected and not option_2_selected:
            option = input("Select the number corresponding to what you would like to do.\n"
            "(1) What is a hashing algorithm?\n"
            "(2) Learn more about the " + selected_algorithm + ".\n"
            "(3) Use " + selected_algorithm + " to hash a password.\n").upper()
        elif not option_1_selected and option_2_selected:
            option = input("Select the number corresponding to what you would like to do.\n"
            "(1) What is a hashing algorithm?\n"
            "(2) Use " + selected_algorithm + " to hash a password.\n").upper()
        elif option_1_selected and not option_2_selected:
            option = input("Select the number corresponding to what you would like to do.\n"
            "(1) Learn more about the " + selected_algorithm + ".\n"
            "(2) Use " + selected_algorithm + " to hash a password.\n").upper()
            option = str(int(option) + 1)
        else:
            option = input("Select the number corresponding to what you would like to do.\n"
            "(1) Use " + selected_algorithm + " to hash a password.\n").upper()
            option = str(int(option) + 2)

        if option in EXIT_STATEMENTS:
            print("Quitting... See you next time!")
            sys.exit(0)
        elif option.strip() == "1" and option_1_selected == False:
            explain_algorithm()
            option_1_selected = True
        elif option.strip() == "2":
            learn_more(selected_algorithm)
            option_2_selected = True
        elif option.strip() == "3":
            print("...", selected_algorithm, "...") # TODO => implement option 3
        else:
            invalid_selection()

def main():
    print_intro()
    selected_algorithm = select_algorithm()
    select_main_features(selected_algorithm)

if __name__ == "__main__":
    main()