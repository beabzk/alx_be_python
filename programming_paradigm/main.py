import sys
import argparse
from robust_division_calculator import safe_divide
from library_management import Book, Library

# Division scenario
def run_division(numerator, denominator):
    result = safe_divide(numerator, denominator)
    print(result)

# Library management scenario
def run_library():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    print("Available books after setup:")
    library.list_available_books()

    print("\nAttempting to check out '1984':")
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    print("\nAttempting to check out '1984' again:")
    library.check_out_book("1984")

    print("\nAttempting to check out 'The Great Gatsby':")
    library.check_out_book("The Great Gatsby")

    print("\nAttempting to return '1984':")
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

    print("\nAttempting to return 'Brave New World' (which was not checked out):")
    library.return_book("Brave New World")

def main():
    parser = argparse.ArgumentParser(description="Division calculator or Library demo")
    subparsers = parser.add_subparsers(dest='command')
    # divide subcommand
    div_parser = subparsers.add_parser('divide', help='Perform a safe division')
    div_parser.add_argument('numerator', help='Numerator for division')
    div_parser.add_argument('denominator', help='Denominator for division')
    # library subcommand
    subparsers.add_parser('library', help='Run library management demo')

    args = parser.parse_args()
    if args.command == 'divide':
        run_division(args.numerator, args.denominator)
    elif args.command == 'library':
        run_library()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()