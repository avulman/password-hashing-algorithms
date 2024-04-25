import sys

print("Welcome to the password hashing program!\n"
       "This program showcases 5 common hashing\n"
       "algorithms including: MD5, SHA-1, SHA-2,\n"
       "NTLM, and LANMAN.\n")

hashing_algorithms = ["MD5", "SHA-1", "SHA-2", "NTLM", "LANMAN"]
exit_statements = ["Q", "QUIT", "EXIT"]

while True:
    option = input("Select an algorithm to learn more or 'Q' to quit:\n").upper()

    if option in hashing_algorithms:
        print("You have selected " + option)
        break
    elif option in exit_statements:
        print("Quitting... See you next time!")
        sys.exit(0)
    else:
        print("Invalid selection. Try again or enter 'Q' to quit.")
selected_algorithm = option

option = input("Select the number corresponding to what you would like to do.\n"
               "(1) What is a hashing algorithm?\n"
               "(2) Learn more about the " + selected_algorithm + "\n")

if option == str("1") or option == str("(1)"):
    print("option 1")
elif option == str("2") or option == str("(2)"):
    print("option 2")