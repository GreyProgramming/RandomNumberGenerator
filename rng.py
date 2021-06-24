import random

# Ask for minimum int
MinInt = int(input("Please enter the minimum integer: "))

#ask for maximum int
MaxInt = int(input("Please enter the minimum integer: "))

#pick random int between the two
print("Your random number is...",random.randint(MinInt, MaxInt))