# Class definition for book
class book():
    def __init__(self, id, bookName, authorName, status):
        self.id = id
        self.bookName = bookName
        self.authorName = authorName
        self.status = status

    # Getter methods
    def get_id(self):
        return self.id

    def get_bookName(self):
        return self.bookName

    def get_authorName(self):
        return self.authorName

    def get_status(self):
        return self.status

    # Setter Methods
    def set_id(self, newVal):
        self.id = newVal

    def set_bookName(self, newVal):
        self.bookName = newVal

    def set_authorName(self, newVal):
        self.authorName = newVal

    def set_status(self, newVal):
        self.status = newVal

    # This method prints out the parameters for book
    def book_details(self):
        print("ID #:", self.id)
        print("Book:", self.bookName)
        print("Author:", self.authorName)
        print("Status:", self.status)
