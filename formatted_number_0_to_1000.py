# Allow the user to input a number while in a loop
while True:
    i = int(input("Enter a number: "))
    
# Set a condition that only allows valid numbers
    if 0 <= i <= 1000:
        break  
    else:
        print("Please enter a valid number.")
        
# Format the input into 6 digits
number = "{:06}".format(i)

# Print result
print(number)