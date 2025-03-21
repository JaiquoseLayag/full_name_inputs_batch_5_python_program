# Allow the user to input a complete statement
# Use the .split() method to split the input into a list of words
staement = input("Enter a statement: ").split()
# Use .isalpha() in a loop to count words only and not numbers
count = 0
for word in statement:
    if word.isalpha()
        count += 1
# Print the result
print(count)