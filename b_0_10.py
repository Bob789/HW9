SENTINEL: int = -999
numbers: list [int] = [] #[5, 0, 2, 7, 2, 1, 9, 5, 2, 0, 10, 2]
while True:
    number: int = int(input('Enter numbers, to exit enter -999 :'))
    if number == SENTINEL:
        break
    if not 0 <= number <= 10:
        continue

    numbers.append(number)
    print()
    for num in numbers:
        print (f" {num}=>{numbers.count(num)}:", end=" ")

print(numbers)