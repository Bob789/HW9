# solution_a
temperatures: list[float] = []

# solution_b
SENTINEL: int = -999

while True:
    temperature: float = float(input('Enter temperature between -50 to 50 :'))
    if temperature == SENTINEL:
        break
    if not -50 <= temperature <= 50:
        continue

    temperatures.append(temperature)

# solution_c
print("solution_c")
list2: list[float] = [18.5, 39.1, -20.0]
temperatures.extend(list2)
print(temperatures, end=" ")

# solution_d
print()
print("solution_d")
list_numbers = [4, 6, 8, 9]
print("Return the real value :", list_numbers + [])  # return value [4, 6, 8, 9]
print("Return None :", list_numbers.extend([]))  # return Nane

# solution_e
print("solution_e")
temperature_max: float = None
temperature_min: float = None
if temperatures:
    temperature_max: float = max(temperatures)
    temperature_min: float = min(temperatures)
else:
    print("The temperatures list is empty. No max or min values can be calculated.")

if temperature_max is not None:
    print("Temperature max:", temperature_max)

if temperature_min is not None:
    print("Temperature min:", temperature_min)

# solution_f
print("solution_f")
temperature_target: float = float(18.5)
if temperature_target in temperatures:
    print(True)
else:
    print(False)

# solution_g
print("solution_g")
temperature_count: int = 0
if temperatures:
    temperature_count = temperatures.count(-20)

print(f"Count -20 : {temperature_count}")

# solution_h
print("solution_h")
if temperatures:
    print("Average :", sum(temperatures) / len(temperatures))
else:
    print("The temperatures list is empty. There is no average")

# solution_i
print("solution_i")
for temp in temperatures:
    print(temp)

# solution_j
print("solution_j")
temperature_target: float = float(39.1)
if temperature_target in temperatures:
    print(f"Index 39.1 : {temperatures.index(temperature_target)}")

# solution_k
print("solution_k")
if temperatures:
    del temperatures[0]

print(f"Del first element :{temperatures}")

# solution_m
print("solution_m")
temperature_target: float = 18.5
for temp in temperatures:
    if temp != temperature_target:
        continue
    else:
        temperatures.remove(temperature_target)
        print(f"The element {temperature_target} is removed")
        print(f"After removing element {temperature_target}: {temperatures}")
        break
else:
    print("There is no element  {temperature_target}")

# solution_n
print("solution_n")
temp_last: float = temperatures.pop()
print(f"the pop {temp_last}")
print(f"list with out {temp_last} {temperatures}")

# solution_o
print("solution_o")
new_list = temperatures.copy()
new_list.sort()
print(f"New list sorted up: {new_list}")

# solution_p
print("solution_p")
new_list = temperatures.copy()
new_list.sort(reverse = True)
print(f"New list sorted down: {new_list}")
