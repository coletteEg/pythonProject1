### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["Shell Silverstein", "Sy Montgomery", "Victor Hugo", "Brandon Sanderson","J.R.R Tolkien", "Rick Riordan", "Jane Austin", "Jordan Peterson"]

# Now let's add a new author to the end with the .append() method. Type your code below.
my_authors.append("Neil Gaiman")
print(my_authors)
# Code here
# Example: my_authors.append("H.G. Wells")


# Now let's remove an element in the list
my_authors.remove("Victor Hugo")
print(my_authors)
# Code here
# Example: my_authors.remove("H.G. Wells")


# Now access an element by it's index. (Remember it indexes start at 0.)
print(my_authors[4])
# Code here
# Example: my_authors[2]


# Now slice the list.
print(my_authors[2:5])
# Code here
# Example: my_authors[1:4]


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.
my_authors_tuple = ("Shell Silverstein", "Sy Montgomery", "Victor Hugo", "Brandon Sanderson","J.R.R Tolkien", "Rick Riordan", "Jane Austin", "Jordan Peterson")
# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###

# Create a set with your authors.
my_authors_set = {"Shell Silverstein", "Sy Montgomery", "Victor Hugo", "Brandon Sanderson","J.R.R Tolkien", "Rick Riordan", "Jane Austin", "Jordan Peterson"}
# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


# Add a new author to your set.
my_authors_set.add("Stephen King")
print(my_author_set)
# Code here
# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.
my_authors_set.add("Stephen King")
# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
print(my_authors_set)


### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.
for name in my_authors:
    print(name)

for name in my_authors_tuple:
    print(name)

for name in my_authors_set:
    print(name)
# Code here
# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

