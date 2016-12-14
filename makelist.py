#TODO: open file
file = open('mylist.txt', 'w')

#TODO: add items to file
for n in range(10):
    file.write(input("What should I add to the list?") + '\n')
    file.write(str(n + 1) + input)
#TODO: close file
file.close()