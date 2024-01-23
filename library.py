import book_list

# I followed and created a similar ATM console based program from this link:
# https://youtu.be/k18L_KxF9Ds?si=ywTVJ7xK06URw096

# This function prints out the entire menu
def print_menu():
    print("Please select from the following options...")
    print("1. Show book list")
    print("2. Search for book by ID number")
    print("3. Return book")
    print("4. Check out book")
    print("5. Exit\n")


# This function prints out all the details (parameters) about the book
def show_books():
    for i in book_list.books:
        i.book_details()
        print("")


# This function gives back all the parameters when book ID is given
def id_search():
    while True:
        try:
            # valid_input checks to see if the number that the user placed is related to a book
            valid_input = False
            inputted_id = int(input(
                "Please enter the ID of the book you would like to look up (type the number 0 to return to menu):"))
            # This for loop
            for i in book_list.books:
                if inputted_id == i.id:
                    i.book_details()
                    return valid_input == True
            if inputted_id == 0:
                return
            elif valid_input == False:
                print("No books have that ID number. Please try again (ID should be a number from 1 to 5).")
        except:
            print("Sorry, no books have that ID (ID should be a number from 1 to 5). ")


# This function turns the status of the books from 'Available' to 'Checked-out'. If already checked out,
# the user will get a print statement that informs them that the book has already been checked out
def check_out():
    while True:
        try:
            get_book = int(
                input("Please enter the ID of the book you would like to check-out (type 0 to return to the menu): "))
            # If the user types the number '0', they will be sent back to the main menu
            if get_book == 0:
                return
            # This for loop goes through the list of books and checks to see whether a book is currently being used
            for i in book_list.books:
                if i.id == get_book and i.get_status() != "Checked-out":
                    i.set_status("Checked-out")
                    return print("You have successfully checked-out!")
                elif i.id == get_book and i.get_status() == "Checked-out":
                    return print("Sorry, that book has already been checked out!")
            # This print statement only shows if the user put in a wrong number instead of a string
            print("Sorry, no books have that number ID. PLease try again.")
        # This print statement is displayed when the user inputs in to the console a non integer value
        except:
            print("Sorry, no books have that ID. Please try again")


# This function sets the status parameter to 'Available' only when the previous status is 'Checked-out'.
# If already containing the 'Available' status, then the user will be informed with a print statement
def return_book():
    while True:
        try:
            give_book = int(input("Please enter the number ID of the book you would like to return (type 0 to return "
                                  "to the menu): "))
            # This allows the user to press '0' and return to the main menu
            if give_book == 0:
                return
            # This increments through the list of book objects and checks whether the user inputted an acceptable value,
            # and the status parameter of the book
            for i in book_list.books:
                if i.id == give_book and i.get_status() != "Available":
                    i.set_status("Available")
                    print("You have returned our book!")
                    return
                elif i.id == give_book and i.get_status() == "Available":
                    print("That book has already been returned")
                    return
            print("Sorry, that number is not a valid book ID. Please try again (input a number from 1 to 5)")
        except:
            print("Sorry, no books have that ID. Please try inputting a NUMBER")


# Main method combines all other functions in order to have a working program
def main():
    print("Welcome to Rincon Library!\n")
    while True:
        option = 0
        while option != 5:
            print_menu()
            try:
                option = int(input())
            except:
                print("Invalid input. Please try entering a NUMBER.")
                break
            if option == 1:
                show_books()
            elif option == 2:
                id_search()
            elif option == 3:
                return_book()
            elif option == 4:
                check_out()
            elif option == 5:
                exit()
            else:
                print("Sorry, that number is not an option. Please select a number from the list.")
                option == 0


main()
