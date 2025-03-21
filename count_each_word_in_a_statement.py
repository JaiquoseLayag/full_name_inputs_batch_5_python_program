# Allow the user to input a complete statement
# Use the .split() method to split the input into a list of words
staement = input("Enter a statement: ").split()
# Use len() to count the number of words in the list
count = len(statement)
# Print the result
print(count)