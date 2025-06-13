lucky_number = [4, 8, 15, 16, 23, 42]
friends = ["kavien", "kamin", "jinny", "jim", "toby", "jim"]

#friends.extend(lucky_number)        # Adds lucky_number elements to friends
friends.append("mark")              # Adds "mark" at the end
friends.insert(1, "peter")          # Inserts "peter" at index 1
friends.remove("kamin")             # Removes the first occurrence of "kamin"
friends.pop()                       # Removes the last item ("mark")

print(friends.count("jim"))         # Count how many times "jim" appears → 2
print(friends.index("kavien"))      # Returns the index of "kavien" → 0

friends.sort()                      # Sorts the list (must be all same type)
lucky_number.sort()                 # Sorts lucky_number in ascending order
lucky_number.reverse()              # Reverses the order → now descending

friends2 = friends.copy()           # Creates a copy of friends
friends.clear()                     # Empties the friends list

print(friends)                      # Should print []
print(lucky_number)                 # Prints reversed sorted numbers
