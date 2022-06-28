my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

newList = my_list[2:9]
for i in my_list:
    if i in newList:
        del my_list[1]
print("La lista con elementos únicos:")
print(my_list)