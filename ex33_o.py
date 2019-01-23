numbers = []
n = int(input())
def add_number(i, n):
    print(f"At the top i  is {i}")
    numbers.append(i)
    i = i + n
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for j in range(0, 360, n):
    add_number(j, n)

for num in numbers:
    print(num)
