# calculator

# Add 
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(s1, s2):
  return s1 - s2
# Multiply
def multiply(m1, m2):
  return m1 * m2
# Divid
def divide(d1, d2):
  return d1 /d2


operations ={
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide

}

num1 = int(input("what is the first number? "))
num2 = int(input("what is the second number? "))
for symbol in operations:
  print(symbol)
operation_sysmbol = input("Pick an operation from the line above: ")

calculation_function = operations[operation_sysmbol]
answer = calculation_function(num1, num2)


print(f"{num1} {operation_sysmbol} {num2} = {answer}" )