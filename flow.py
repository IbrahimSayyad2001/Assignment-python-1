# Write a program for students to declare their result 

marks= int( input('Enter your marks'))
if marks>= 70 :
    print('you got first class ')
elif marks>= 50:
        print('you got second class')
elif marks>= 40:
            print('you just passed')
else :
                print ('you have failed ')
__________________________________________

# wap to identify employees according to their salaries

salary=int(input('Enter salary'))
if salary >=200000: 
    print(' manager')
elif salary>=150000:
    print(' senior employee')
elif salary>=100000:
    print (' junior employee')
elif salary>=30000:
    print ('fresher employee ')
else :
    print (' intern employee ')
__________________________________________

#Define number is even or odd 

num= int(input('Enter the number:'))
if num %2==0:
    print('The number is Even number ')
else: 
    print ('The number is Odd number ')

__________________________________________

# wap to define number is positive or negative 
nm=int(input('Enter the number'))
if nm>0:
    print('Number is positive ')
elif nm<0:
    print('Number is negative ')
else :
    print('Number is zero')

_________________________________________

# wap to identify the character is vowel or consonant

char=input('Enter a character :').lower()
if char in 'aeiou':
    print('Vowel')
else :
    print('Consonant')
__________________________________________
#Define the function to check the colour of the traffic signal

traffic_colour = input('Enter the colour of the traffic signal: ')

if traffic_colour == 'red':
    print('Stop the vehicle')
elif traffic_colour == 'yellow':
    print('Lower the speed of vehicle to stop')
elif traffic_colour == 'green':
    print('Vehicle Keep Going')
else:
    print('Invalid colour')
    
