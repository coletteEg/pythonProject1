### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here



def create_new_book():
  title = input("Tell me the title of the book you would like to add - ")
  author = input("Tell me the author of the book you would like to add - ")
 try:
    year = int(input("What year was this book published? - "))
except:
    year = int(input("Please type a number for the year? - "))
try:
    rating = float(input("what would you rate this book out of 5? - "))
except:
    rating = float(input("please insert a number for the rating, ex: 3.5 - " ))
try:
    pages = int(input("How many pages are in the book? - "))
except: 
    pages = int(input("please insert a whole number of how many pages are in the book, ex: 134 - "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary

def print_all_books(list_of_books):

    print("Here are your books...\n")

    for book in list_of_books:
        title = book["title"]
        author = book["author"]
        year = book["year"]
        rating = book["rating"]
        pages = book["pages"]

        print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")


def main_menu(books_source):

    active = True

    while active:
        choice = input("\nChoose 1 to add a book...\nChoose 2 to see all your books...\nChoose 3 to see a count of your books...\nChoose 4 to see a count of the pages of your books...\nChoose 5 to exit.\nType here: ")

        if choice == "1":
            books_source.append(create_new_book())
        elif choice == "2":
            print_all_books(books_source)
        elif choice == "3":
            print(f"You have a total of {len(books_source)} books.")
        elif choice == "4":
            print(f"Here are the number of pages in all your books {sum([x['pages'] for x in books_source])} pages!")
        elif choice == "5":
            print("Goodbye")
            active = False
        else:
            print("Sorry please type a number for one of the options.")

main_menu(current_books)


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here---- fixed it above



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

#fixed above

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
# if condition_1:
#     # executes when condition one is truthy, exits the if-block
# elif condition_2:
#     # executes only if condition_1 is not truthy
# else:
    # executes if both condition_1 and condition_2 are falsy.

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

# while condition:
#     run_code()
