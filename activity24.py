def GreetUser(name):
  print(f"Hi {name}, kamusta kana? ")

def summation(i):
  sum = 0
  for x in range(i,0,-1):
    sum += x
  print(f"The sum of {i} is {sum}")

if __name__ == "__main__":
  GreetUser("Donn")
  GreetUser("H")
  summation(18)