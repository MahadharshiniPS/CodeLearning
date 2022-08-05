weight = input("Enter your weight in pounds: ")
converted_kilogram = float(weight) * 0.45359237
print(converted_kilogram)

numbers = [5,2,5,2,2]
for number in numbers:
    print(number * 'x')

list = [1000,5,6,3,9,13]
max = list[0]
for lists in list:
    if lists > max:
        max = lists
print(f"{max} is the largest")

list =[1,4,10,5,4,3,1,5,8]
duplicates = []
for i in list:
    if i not in duplicates:
        duplicates.append(i)
print(duplicates)
