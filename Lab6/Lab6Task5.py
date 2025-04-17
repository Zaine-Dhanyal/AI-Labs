import numpy as np
A = np.array([10, 20, 30, 40, 50])
num = int(input("Enter a number to check: "))
if num in A:
    print(f"{num} is present in the array.")
else:
    print(f"{num} is not present in the array.")

