'''
print('Luck Game.. ')
num=5
b=int(input('Enter a number from 1 to 10 : '))
while num!=b:
    b=int(input('guess a number between 1 to 10'))
else:
    print('Great ! You did it')
'''
'''
حل اخر
'''
print('Luck Game.. ')
num=5
b=int(input('guess the number between 1 to 10 : '))
while True:
    if b>10 or b<1:
    print('guess a number between 1 to 10'))
    b=int(input('guess the number between 1 to 10 : '))
else:
    while b!=num:
        b=int(input('guess the number between 1 to 10 : '))
    else:
        print('Great!! you win')
        break
