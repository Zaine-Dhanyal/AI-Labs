letter = input('Enter a letter ')
if letter in 'aieou':
    print(f'{letter} is a vowel')
elif letter.isalpha():
    print(f'{letter} is consonant')
else:
    print('Invalid input')
