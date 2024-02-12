def evaluate(eqn_input, x, y):
    equation = lambda x, y: eval(eqn_input)
    return equation(x, y)

def satisfied(y1, y2):
    y1 = int(y1 * 10000)
    y2 = int(y2 * 10000)
    return y1 == y2

h = float(input("Enter Δx or h: "))
y0 = float(input("Enter y0: "))
x0 = float(input("Enter x0: "))
x = float(input("Enter x for which the function has to be evaluated: "))
eqn_input = input("Provide equation f(x, y) or dy/dx: ")

outer_loop = int((x - x0) / h)
y1 = y0

while outer_loop > 0:
    outer_loop -= 1
    y2 = y0 + h * evaluate(eqn_input, x0, y1)
    while not satisfied(y1, y2):
        y2 = y0 + (h * (evaluate(eqn_input, x0, y0) + evaluate(eqn_input, x0, y1)) / 2)
        y1 = y2

print(f"y({x}) = {y2}")