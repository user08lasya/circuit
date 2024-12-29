def circuit_output(A, B, C):
    # Logic Gates
    and1 = A and B
    or1 = B or C
    and2 = C and or1
    and3 = A and or1
    or2 = and1 or and2 or and3
    return or2
inputs = [
    (0, 0, 0), 
    (0, 0, 1), 
    (0, 1, 0), 
    (0, 1, 1), 
    (1, 0, 0), 
    (1, 0, 1), 
    (1, 1, 0), 
    (1, 1, 1)
]

for A, B, C in inputs:
    result = circuit_output(A, B, C)
print(f"A={A}, B={B}, C={C} => Q={result}")