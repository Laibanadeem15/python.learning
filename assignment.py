import math
name = input("Enter your name")
print(f"Hello, {name}! Let's explore your favourite number")

numbers = []

for i in range(1, 4):
    num = int(input(f"Enter your {i} favourite number"))
    numbers.append(num)

num_check_list = []  # Moved outside of the loop

for num in numbers:
    if num % 2 == 0:
        num_check_list.append(f"The {num} is even")
    else:
        num_check_list.append(f"The {num} is odd")

# Print the results of even/odd check
for statement in num_check_list:
    print(statement)

# Calculate and print squares
for num in numbers:
    square = num ** 2
    print(f"The number {num} and its square: ({num}, {square})")

# Calculate the sum of numbers
total_sum = 0
for num in numbers:
    total_sum += num

print(f"Amazing! The sum of your favorite numbers is: {total_sum}")
is_prime = True
if total_sum <= 1:
    is_prime = False
else:
    for i in range(2,int(math.sqrt(total_sum))+1):
        if total_sum % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"Wow! The sum {total_sum} is a prime number!")
else:
    print(f"The sum {total_sum} is not a prime number!.")
