# Do not modify this code
class InvalidBookNameException(Exception):
    pass

# TODO: Implement the validate method inside the BookNameValidator class
class BookNameValidator:
    @staticmethod
    def validate(book_name):
        # code here
        if book_name.startswith('Scaler Java'):
            print(f'Book created!: {book_name}')
        else:
            raise InvalidBookNameException("Book name doesn't start with Scaler Java")


