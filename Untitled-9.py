
book_list = []
book_list_futher = []


book1 = input("Enter the name of a book you own: ")
another_book = input("Enter the name of another book you own(or press 'Enter' o skip ): ")

if book1:
    book_list.append(book1)
if another_book:
    book_list.append(another_book)

print(f"Your Library: {book_list}")

Book3 = input("Enter the name of a book you wish to have in the future: ")
Book4 = input("Enter the name of another book you wish to have (or press 'Enter to skip'): ")

if Book3:
    book_list_futher.append(Book3)
if Book4:
    book_list_futher.append(Book4)

print(f"Your Wishlist: {book_list_futher}")

Book5 = input("Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")

if Book5 in book_list_futher:
    book_list_futher.remove(Book5)
    book_list.append(Book5)


print(f"Updated Library: {book_list}\n")
print(f"Updated Wishlist: {book_list_futher}")

Book6 = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")

if Book6 in book_list:
    book_list.remove(Book6)
    
print(f"Final Library after Donations: {book_list}")


