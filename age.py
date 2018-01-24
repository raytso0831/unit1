#Ray Tso
#1/22/18
#age.py

phrase= input('enter first and last name:')
age=int(input('enter your age:'))
first,last=phrase.split()

print('Number of letters in your first name:',len(first))
print('Number of letters in your first name:',len(last))
print(' Next year you will be', age+1)