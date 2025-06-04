def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item: # Ensure item is not empty
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            else:
                print(f"Item '{item_to_remove}' not found in the list.")
        elif choice == '3':
            if not shopping_list:
                print("The shopping list is currently empty.")
            else:
                print("\n--- Your Shopping List ---")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
                print("------------------------")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()