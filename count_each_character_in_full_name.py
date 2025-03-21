# Allow the suer to input their full name
full_name = input("Enter your full name: ")
# Use len() function to count each letter
# Use .replace() to remove spaces in the input
count = len(full_name.replace(" ", ""))
# Print result
print(count)