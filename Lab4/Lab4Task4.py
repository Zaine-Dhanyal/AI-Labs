num = int(input('Enter a non negative integer'))
factorial =1
if num < 0:
    print('Please enter non negative integer')
else:
    i=num
    while i >1:
        factorial *= i
        i-=1
result = factorial
print(f'The factorial of {num} is {factorial}')
