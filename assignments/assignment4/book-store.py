#Author: Drew Rafferty

print("***** Welcome to our bookstore *****")

display = input("What would you like to do (V)iew or (O)rder: ").lower().strip()

if display == "v":
    print("""Our catalogue consists of:
    - 1984 by George Orwell
    - The Help by Kathryn Stockett
    - Gone with the Wind by Margaret Mitchell
    - The Fellowship of the Ring by J.R.R. Tolkien
    """)
elif display == "o":
    bName = input("Enter book name: ")
    if bName == "The Help":
        print("You can buy The Help for $7.59")
    elif bName == "1984":
        print("You can buy 1984 for $9.99")
    elif bName == "Gone with the Wind":
        print("You can buy Gone with the Wind for $8.50")
    elif bName == "The Fellowship of the Ring":
        print("You can buy The Fellowship of the Ring for $10.11")
    else:
        print("Invalid Response. Exiting Now.")
else:
    "Invalid Response. Exiting Now."
print("Have a nice day")