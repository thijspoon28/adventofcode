input_file = open('input.txt', "r")  # opens the file in read mode
input = [(line) for line in input_file.read().splitlines()]
input_file.close()


y = 0
tree=0

print(input)


for i in input:
    if y > 30:
        y -= 31
    if i[y] == '#':
        tree += 1
    print(i[y])
    print(tree)
    y += 3
   
    

#answer = 259

