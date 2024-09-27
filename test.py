# numbers: list[int] = []
# height: float = None
# for i  in range(1,50+1):
#     numbers.append(i)
#
# sum_list: int = sum(numbers)
# avg_list: float = sum_list/len(numbers)
# print("Sum_avg : {avg_list}")
#
# height_list: list[float] = [1.25, 1.1, 2.2 ,2.25, 3.4, 5.6, 1.9]
# for height in
# import random
# numbers: list[int] = []
#
# for i  in range(20):
#     number: int = random.randint(-50,50)
#     numbers.append(number)
#
# print(numbers)
# for number in numbers:
#     if number > 0:
#         print(f" {number} ",end=" ")


# list_names = []
#
# while True:
#
#     name: str = str(input("Enter name :"))
#     if name == "exit":
#         break
#     if  name in list_names:
#         continue
#     list_names.append(name)
#
#
# print(list_names)


# list_names = [4, 6, 8, 9]
#
# list_names.extend([4, 8, 1])
# print(list_names)

list_numbers = [4, 6, 8, 9]
print(list_numbers+[]) #return value [4, 6, 8, 9]
print(list_numbers.extend([])) #return Nane