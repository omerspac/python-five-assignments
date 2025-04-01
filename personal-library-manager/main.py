import json

class BookCollection:
    """A class to manage a collection of books, allowing users to store and check reading materials!"""

    def __init__(self): # constructor
        """Initialize a new book collection with an empty list and setting up file storage."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Loads saved books from a JSON file into memory. If the file doesn't exist or is corrupted then it will just create an empty collection."""
        try:
             with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Stores the current book collection to JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent = 4)

    def create_new_book(self):
         """Adds a new book to the collection by gathering information from the user."""
         book_title = input("Enter the book title: ")
         book_author = input("Enter the author: ")
         book_publication_year = input("Enter the publication year: ")
         book_genre = input("Enter the genre: ")
         is_book_read = (
            input("Have you read this book? (yes/no) ").strip().lower() == "yes"
         )

         new_book = {
            "title": book_title,
            "author": book_author,
            "year": book_publication_year,
            "genre": book_genre,
            "read": is_book_read
         }

         self.book_list.append(new_book)
         self.save_to_file()
         print("Book added successfully!\n")

    def delete_book(self):
        """Deletes a book from the collection by using book title."""
        book_title = input("Enter the title of the book to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book removed successfully!\n")
                return
        
        print("Book not found!\n")
    
    def search_book(self):
        """Searches a book in the JSON file by either using title or author name."""
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter search term: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]

        if found_books:
            print("Matching Books: ")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                )
        else:
            print("No matching books found!")

    def display_all_books(self):
        """Displays all the books stored in JSON."""
        if not self.book_list:
            print("Your collection is empty.\n")
            return

        print("Your Book Collection:")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
            )
        print()

    def display_stats(self):
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (
            (completed_books / total_books * 100) if total_books > 0 else 0
        )
        print(f"Total books: {total_books}")
        print(f"Percentage read: {completion_rate:.2f}%\n")

    def exit_program(self):
        """Exit the program by saving everything"""
        self.save_to_file()
        print("Library saved to file. Goodbye!")

    def start_application(self):
        """Runs the application"""
        while True:
            print("Welcome to your Personal Library Manager!")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")

            user_input = input("Enter your choice (1-6): ").strip()
            if user_input == "1":
                self.create_new_book()
            elif user_input == "2":
                self.delete_book()
            elif user_input == "3":
                self.search_book()
            elif user_input == "4":
                self.display_all_books()
            elif user_input == "5":
                self.display_stats()
            elif user_input == "6":
                self.exit_program()
                break
            else:
                print("Invalid choice. Try again!\n")

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()