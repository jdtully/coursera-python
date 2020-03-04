def count_letters(words):
    result = {}
    for letter in words:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


print(count_letters("Dictionaries are mutable, meaning they can be modified by adding, removing, and replacing elements in a dictionary, similar to lists. You can add a new key value pair to a dictionary by assigning a value to the key, like this: animals This creates the new key in the animal dictionary called zebras, and stores the value 2. You can modify the value of an existing key by doing the same thing. So animals would change the value stored in the bears key from 10 to 11. Lastly, you can remove elements from a dictionary by using the del keyword. By doing del animals you would remove the key value pair from the animals dictionary."))
