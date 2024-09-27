SENTINEL: int = -999
numbers: list [int] = []#[0, 60, 14, 79, 100, 26, 53, 11, 3, 77, 42, 2, 3, 90, 79, 17, 50, 32, 64, 71, 3, 89, 83, 97, 2, 91, 72, 53, 53, 24, 2, 100, 38, 57, 35, 88, 80, 1, 15, 91, 13, 17, 85, 90, 62, 31, 10, 32, 79, 9, 77, 3, 75, 35, 100, 13, 5, 16, 27, 58]

index_list_counter: list [int] = []
LEN_LIST: int = 100
while True:
    number: int = int(input('Enter numbers, to exit enter -999 :'))
    if number == SENTINEL:
        break
    if not 0 <= number <= LEN_LIST:
        continue

    numbers.append(number)


print()
index_list_counter = [0] * 101

for num in numbers:
    index_list_counter[num] = numbers.count(num)

print(numbers)
print(index_list_counter)