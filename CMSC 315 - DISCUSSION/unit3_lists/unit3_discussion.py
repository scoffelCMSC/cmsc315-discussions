"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # When you insert a value using .insert(), it shifts all values from the specified index and higher one position to the right.
    # Inserting at the beginning of the list would cause the most possible shifts, and the least at the end. 
    # More shifts in the index would have a larger impact on performance than one at the end.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.

    """
    # Index validation allows for crashes due to invalid inputs to be avoided, and allows for handleable edge cases.
    # Checks to see if the index is valid to avoid a crash.
    if 0 <= index < len(lst):
        # Removes the item from the list and returns it.
        return lst.pop(index)

    # If the index is invalid, returns None here
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This goes through a list in a sequential manner, which makes it linear.
    # As a loop it will iterate through all values in the list to return the specified value.
    for index in range(len(lst)):
        if lst[index] == value:
            return index
    # -1 serves as an indication that the value we were looking for isn't present.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # Initialize list. Five items in total to start 
    warlock_inventory = ["Astrocyte Verse", "The Stag", "Felwinter's Helm", "Winter's Guile", "Nezarec's Sin"]
    # Display the original list as a reference point
    print(f"Warlock Inventory (Original): {warlock_inventory}")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    
    print("\n=== INSERTION TESTS ===")

    # Inserting items at the head, middle, and tail.
    # This puts our item in at the given index, and shifts all items after the specified index forward.
    # First insertion shifts all items in the list forward, as every index from 0 and up must be moved.
    insert_at(warlock_inventory, 0, "Verity's Brow")
    print(f"After adding to the front of the inventory: {warlock_inventory}")
    # Insertion at the middle of the list is 3, which is the fourth item. 
    # This shifts every index after 3 forward.
    insert_at(warlock_inventory, 3, "Soliprism")
    print(f"After adding to center of the inventory: {warlock_inventory}")
    # Inserting at the end of the list does not shift any items another index
    # There is nothing in front of the end of the list to shift forward.
    insert_at(warlock_inventory, len(warlock_inventory), "Aeon Soul")
    print(f"After adding to the end of the inventory: {warlock_inventory}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # The first pop will be indicated to be at the index's current front.
    # The deleted item is stored in popped_start to be printed later when called.
    # The new list is then printed afterwards.
    popped_start = delete_at(warlock_inventory, 0)
    print(f"Removed from inventory: {popped_start}")
    print(f"New Warlock Inventory: {warlock_inventory}")
    # The middle item is then deleted, stored, and printed along with the updated list.
    popped_mid = delete_at(warlock_inventory, 3)
    print(f"Removed from inventory middle: {popped_mid}")
    print(f"New Warlock Inventory: {warlock_inventory}")
    # The last item is deleted from the end of the list.
    popped_end = delete_at(warlock_inventory, len(warlock_inventory) - 1)
    print(f"Removed from inventory end: {popped_end}")
    print(f"New Warlock Inventory: {warlock_inventory}")


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Searching for an existing value
    locate_armor = search_value(warlock_inventory, "The Stag")
    # If/else that produces the results. If the item is found, it will print the index for that item.
    if locate_armor != -1:
        print(f"Armor found at index: {locate_armor}")
    else:
        print("Armor does not exist.")
    # Searching for a value that doesn't exist
    locate_armor = search_value(warlock_inventory, "Contraverse Hold")
    # The if/else is the same here, as it handles if the value does or doesn't exist in the previous search.
    if locate_armor != -1:
            print(f"Armor found at index: {locate_armor}")
    else:
        print("Armor does not exist.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Case 1: Deleting from an empty list.
    # Attempts to delete an item from an empty list
    my_list = []
    eat_list = delete_at(my_list, 5)
    print(f"Attempting to delete from an empty list returns {eat_list} and the list is now: {my_list}")

    # Case 2: Searching for a value that doesn't exist, again
    # Attempts to find a value that is not present in the list.
    second_list = ["Matadoxia", "Briarbinds"]
    finder = search_value(second_list, "Contraverse Hold")
    print(f"Attempting to search for an item that does not exist yields: {finder}")




if __name__ == "__main__":
    main()