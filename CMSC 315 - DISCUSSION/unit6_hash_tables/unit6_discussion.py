"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")
    # Create the empty dictionary. Weapon list with their IDs.
    weapons = {}
    # The weapon name is our key, as a string, and our weapon IDs are integers. 
    weapons["Alethonym"] = 1001588
    weapons["Polaris Lance"] = 1000323
    weapons["Lord of Wolves"] = 1000045
    weapons["Divinity"] = 1001223
    weapons["Choir of One"] = 1001704

    # Python dictionaries are innately implemented using a hash map

    for key in weapons:
        print(f"Weapons: {key}: {weapons[key]}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # A lookup converts the key into a hash to make the lookup speed only O(1).
    # It uses the hash to determine a location and then performs the comparison.
    weapon_list = ["Divinity", "Polaris Lance"]

    for weapon in weapon_list:
        print(f"{weapon} has the ID of {weapons[weapon]}")


    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")
    # Creating and updating a key use the same operation since duplicate keys cannot exist. 
    print(f"Weapon ID for test build: {weapons['Alethonym']}")
    # Our new value is created.
    weapons["Alethonym"] = 1000777
    # The previous key is now overwritten by the new one.
    print(f"Updated Weapon ID: {weapons['Alethonym']}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print(f"Weapon list, pre-deletion: {weapons}")
    # Pop would save the value for later if we needed to see what we deleted.
    # del would remove it permanently without an ability to reference to it.
    weapons.pop("Divinity")
    print(f"Weapons after deletion: {weapons}")
    # Deleting a key-value pair removes both from the dictionary. 
    # If the key is deleted from a map, the length of the map is decreased by 1.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Missing Key Lookup
    # An error will occur, as the key cannot be found.
    print("Edge Case 1: Missing Key Lookup")
    print(f"Current Weapon List: {weapons}")
    print(f"Weapon Lookup - Hierarchy of needs: {weapons['Hierarchy of Needs']}")

    # Edge Case 2: Missing Key Update
    # Updating the value for a missing key will add it to the list, as the operations are the same.
    print(f"Current Weapon List: {weapons}")
    weapons["Hierarchy of Needs"] = 1011059
    print(f"New Weapons List: {weapons}")


if __name__ == "__main__":
    main()