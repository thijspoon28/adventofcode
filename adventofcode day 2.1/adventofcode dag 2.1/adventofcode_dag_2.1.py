input_file = open('input.txt', "r")  # opens the file in read mode
input = [(line) for line in input_file.read().splitlines()]
input_file.close()

def password():
    for x in input:
        print(x)



print(password())

print(input[1].index('-'))
print(input[0].index(':'))
print(input[0].index(' '))

d = (input[1].index('-'))
t = (input[0].index(':'))
s = (input[0].index(' '))

case = 0

def first_number():
    number1 = ''
    for i in input[case]:
        number1 += str(i)
        print(number1)
        if i > d:
            print(number1)
            break


  
print(first_number())
