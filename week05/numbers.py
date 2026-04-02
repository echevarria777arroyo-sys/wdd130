numbers = []

print("Enter a list of numbers, type 0 when finished.")

while True:
    num = int(input("Enter number: "))

    if num == 0:
        break

    numbers.append(num)

# Outside the loop
total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)

smallest_positive = None

for num in numbers:
    if num > 0:
        if smallest_positive is None or num < smallest_positive:
            smallest_positive = num

print("The sum is:", total)
print("The average is:", average)
print("The largest number is:", largest)

if smallest_positive is not None:
    print("The smallest positive number is:", smallest_positive)
else:
    print("No positive numbers were entered.")

    