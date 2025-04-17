num = int(input('Enter your salary:'))
num1 = int(input('Enter your years of service:'))
if num1 > 5:
    bonus = num*0.05
    print(f'Your bonus is {bonus}')
else:
    print('Your are not eligible')
print(bonus + num)