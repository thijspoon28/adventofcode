input_file = open('input.txt', "r")  # opens the file in read mode



def input_lines():
    line = True
    string = ''
    list = []
    sortlist = []
    count = 0
    while line:
        line = input_file.readline()
        if line != "\n":
            line = line.rstrip()
            string = line + string
            print(string)
        else:
            for i in string:
                list.append(i)
                list.sort()
                string = ''
            for x in list:
                if x != double:
                    count += 1
                double = x
            print(count)
            print(list)
            list = []
        double = ''
            

        

input_lines()