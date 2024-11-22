from collections import deque

number_collection = deque()

list_of_numbers = input()
numbers_chosen = []

for num in list_of_numbers.split():
    numbers_chosen.append(int(num))

for num in numbers_chosen:
    number_collection.append(num)
print(deque(number_collection))

while number_collection:
    num = number_collection.pop()
    print(num * num)
