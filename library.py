def main():
    welcome()
    my_books = get_books()
    my_ratings = get_ratings(my_books)
    print("\n")
    print_library(my_books, my_ratings)


def welcome():
    print("\033[H\033[J")
    print("#" * 26)
    print("Personal Library Assistant")
    print("#" * 26)
    print("\n")

def get_books():
    books = []
    book_title = input("Enter a book title: ")

    while book_title != "":
        books.append(book_title)
        book_title = input("Enter another book title: ")
    
    return books

def get_ratings(books):
    ratings = []
    for book_title in books:
        rating = input("How would you rate '" + book_title + "'? (1-5)\n")
        ratings.append(rating)
    
    return ratings

def print_library(books, ratings):
    num_books = len(books)
    print("\033[H\033[J")
    print("#" * 18)
    print("My library: " + str(num_books) + " books")
    print("#" * 18)
    #print("\n")

    for book_index in range(num_books):
        print(books[book_index] + ": " + ratings[book_index] + "/5")

    print("\n")



main()