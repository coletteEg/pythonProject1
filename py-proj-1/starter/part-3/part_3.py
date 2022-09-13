my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book_list = [
    {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}, 
{
    "title": "The Giving Tree",
    "author": "Shell Silverstein",
    "year": 1964,
    "rating": 4.8,
    "pages": 57
},
{
    "title": "The Soul of an Octopus",
    "author": "Sy Montgomery",
    "year": 2019,
    "rating": 4.0,
    "pages": 197
},
{
    "title": "Lord of the Rings",
    "author": "J.R.R Tolkien",
    "year": 1954,
    "rating": 5.0,
    "pages": 1137
},
{
    "title": "Little Women",
    "author": "Louisa May Alcott",
    "year": 1869,
    "rating": 4.5,
    "pages": 280
}
]

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def books_function(book_dictionary):
    book_sentence = f" The title of this book is {book_dictionary['title']}, and was written by {book_dictionary['author']}. Published in {book_dictionary['year']} and has a rating of {book_dictionary['rating']}. This book is {book_dictionary['pages']} pages long."
    return book_sentence

    print(books_function(my_book))



# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def return_year(book_dictionary):
    year = book_dictionary['year']
    return year
    print(return_year(my_book))

def return_pages():
    pages_number = book_dictionary['pages']
    return pages_number
    print(return_pages(my_book))

def return_authors(book_dictionary):
    author = book_dictionary['author']
    return author

    print(return_authors(my_book))
    
def return_rating():
    book_rating = book_dictionary['rating']
    return book_rating

    print(return_rating(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def get_authors(book_dicitonary_list):
    authors = set()

    for book_dictionary in 
    book_dictionary_list:
        authors.add(book_dictionary['author'])
        return authors

def get_pages(book_dictionary_list):
    pages = 0

    for book_dictionary in
    book_dictionary_list:
    pages += book_dictionary['pages']
    return pages

def total_books(book_dictionary_list):

    for book_dictionary in
    book_dictionary_list:
    print(total_books(book_dictionary))