#String Concatenation

first = 'Donn Romuelle'
mid = 'B'
last = 'Balmaceda'

print("My name is " , first," ", mid," ",last)

#String Formatting

fn = 'Donn Romuelle'
mn = 'B'
ln = 'Balmaceda'

print(f"My name is {fn} {mn} {ln} ")

#For Upper & Lower Case
fnm = 'Donn Romuelle'
mnm = 'B' 
lnm = 'Balmaceda' 

print(f"My name is {fnm.upper()} {mnm.upper()} {lnm.upper()} {10 + 8}") 
print(f"My name is {fnm.lower()} {mnm.lower()} {lnm.lower()} {10 + 8}") 

#Summation
sum = 0
for x in range(1, 11, 1):
    num = eval(input(f" {x} - Input any number: "))
    sum += num
print(f"The total sum of all the numbers is {sum} ") 