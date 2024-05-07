import sys
import time
import hashlib
import secrets

EXIT_STATEMENTS = ["Q", "QUIT", "EXIT"]
HASHING_ALGORITHMS = ["MD5", "SHA-1", "SHA-2", "NTLM", "LANMAN"]

def print_intro():
    print("╔═══════════════════════════════════════════════╗\n"
          "|   Welcome to the password hashing program!    |\n"
          "╞═══════════════════════════════════════════════╡\n"
          "|   This program showcases 5 common hashing     |\n"
          "|   algorithms including: MD5, SHA-1, SHA-2,    |\n"
          "|   NTLM, and LANMAN.                           |\n"                        
          "╚═══════════════════════════════════════════════╝\n")

def explain_algorithm():
    print("\nYou selected: » What is a hashing algorithm? «\n")
    print("Hashing is a one-way function to scramble data — it takes\n"
        "readable text and transforms it into a completely different\n"
        "string of characters with a set length. However, unlike other\n"
        "encryption algorithms that transform data, hashing is nearly \n"
        "impossible to revert.\n")

def invalid_selection():
    print("Invalid selection. Try again or enter 'Q' to quit.")

def learn_more(selected_algorithm):
    print("You selected » Learn more about the", selected_algorithm + " «\n")

def hash_password(selected_algorithm):
    option_1_selected = False
    salt_enabled = False
    print("\nYou selected » Hash a password using", selected_algorithm, "«\n")
    password_to_hash = ""
    while not password_to_hash:
        password_to_hash = input("Select a password that is 1-16 characters in length.\n"
                                   "* Password you would like to hash: ")
        if not password_to_hash:
            print("Password must be at least 1 character.")
        elif len(password_to_hash) > 16:
            print("Password exceeds length criteria.")
        else:
            while not option_1_selected == True:
                option = input("\n(1) Add a salt. \n"
                    "(2) Do not add a salt.\n"
                    "(3) What is a salt?\n"
                    "* Select an option: ")
                if option == "3":
                    print("A salt is a randomly generated string of characters that\n"
                        "is added to a password before it is hashed. The purpose of\n"
                        "adding a salt is to enhance the security of hashed passwords,\n"
                        "particularly against dictionary and rainbow table attacks.\n")
                    option_1_selected = True
                elif option == "1":
                    print("\nSalting your password!")
                    pre_salt_password = password_to_hash
                    salt = generate_salt()
                    password_to_hash = salt_password(password_to_hash, salt)
                    salt_enabled = True
                elif option == "2":
                    print("No worries.")
                else:
                    invalid_selection()

                print("Password:", pre_salt_password)
                if salt_enabled == True:
                    print("Salt:", salt)
                    salt_enabled = False

                print("Hashing »", password_to_hash, "«\n")
                hashed_password = md5(password_to_hash)
                print(selected_algorithm, "Hashed Password: »", hashed_password, "«\n")
                break

def generate_salt():
    return secrets.token_hex(8) # generate a random salt of 16 bytes

def salt_password(password_to_hash, salt):
    password_to_hash = password_to_hash + salt # concatenate the password and the salt
    return password_to_hash # return password with salt

def md5(password_to_hash):
    md5_hasher = hashlib.md5() # create MD5 hash object
    md5_hasher.update(password_to_hash.encode('utf-8')) # update the hash object with the bytes-like object (encoded text)
    hashed_password = md5_hasher.hexdigest() # get the hexadecimal digest of the hash

    return hashed_password

def selected_statement(option):
    print("\nYou selected »", option, "«\n")

def select_algorithm():
    while True:
        option = input("* Enter an algorithm to learn more or 'Q' to quit:\n").upper()
        if option in EXIT_STATEMENTS:
            print("Quitting... See you next time!")
            sys.exit(0)
        elif option in HASHING_ALGORITHMS:
            selected_statement(option)
            return option
        #else:
            #invalid_selection() # temporarily disabled. prints invalid_selection and "enter an algorithm to..."
            # TODO Fix double message when invalid selection is made.

def select_main_features(selected_algorithm):
    option_1_selected = False
    option_2_selected = False
    while True:
        if not option_1_selected and not option_2_selected:
            option = input("(1) What is a hashing algorithm?\n"
            "(2) Learn more about the " + selected_algorithm + ".\n"
            "(3) Use " + selected_algorithm + " to hash a password.\n"
            "* Select the number corresponding to what you would like to do: ").upper()
        elif not option_1_selected and option_2_selected:
            option = input("(1) What is a hashing algorithm?\n"
            "(2) Use " + selected_algorithm + " to hash a password.\n"
            "* Select the number corresponding to what you would like to do: ").upper()
        elif option_1_selected and not option_2_selected:
            option = input("(1) Learn more about the " + selected_algorithm + ".\n"
            "(2) Use " + selected_algorithm + " to hash a password.\n"
            "* Select the number corresponding to what you would like to do.").upper()
            option = str(int(option) + 1)
        else:
            option = input("(1) Use " + selected_algorithm + " to hash a password.\n"
            "* Select the number corresponding to what you would like to do: ").upper()
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
            hash_password(selected_algorithm)
        else:
            invalid_selection()

def main():
    # TODO implement to loop program in a clean manner.
    # completed_program = False 
    print_intro()
    selected_algorithm = select_algorithm()
    select_main_features(selected_algorithm)

if __name__ == "__main__":
    main()
