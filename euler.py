def evaluate(eqn_input, x, y):
    equation = lambda x, y: eval(eqn_input)
    return equation(x, y)

h = float(input("Enter Δx or h: "))
y0 = float(input("Enter y0: "))
x0 = float(input("Enter x0: "))
x = float(input("Enter x for which the function has to be evaluated: "))
eqn_input = input("Provide equation f(x, y) or dy/dx: ")
loop = int((x - x0) / h)

y = y0
x1 = x0

while loop > 0:
    loop -= 1
    y = y + h * evaluate(eqn_input, x1, y)
    x1 += h
    
print(f"y({x}) = {y}")