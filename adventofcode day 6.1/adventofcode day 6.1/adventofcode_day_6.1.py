input_file = open('input.txt', "r")  # opens the file in read mode



def input_lines():
    line = True

   
    while line:
        line = input_file.readline()
        if line != "\n":
            print(line)

        

input_lines()